#include <Windows.h>
#include <Shlwapi.h>
#include <Stdio.h>
#include <Tchar.h>
#include <atlbase.h>
#include <imapi2fs.h>
#include <sys/stat.h>

#pragma comment(lib, "Shlwapi.lib")

VOID SaveIso(LPWSTR pSrcDir, LPWSTR pIsoPath)
{
    HRESULT hr;
    IFileSystemImage* pSystemImage = nullptr;
    IFsiDirectoryItem* pRootDirItem = nullptr;
    IFileSystemImageResult* pSystemImageResult = nullptr;
    IStream* pImageStream = nullptr;
    IStream* pFileStream = nullptr;

    // 创建文件系统镜像对象
    hr = CoCreateInstance(__uuidof(MsftFileSystemImage),
        NULL,
        CLSCTX_INPROC_SERVER,
        __uuidof(IFileSystemImage),
        (LPVOID*)&pSystemImage);
    if (FAILED(hr)) {
        printf("[-] Failed to create FileSystemImage instance (0x%x)\n", hr);
        return;
    }

    // 设置文件系统类型（推荐同时支持 UDF, Joliet, ISO9660）
    hr = pSystemImage->put_FileSystemsToCreate(
        (FsiFileSystems)(FsiFileSystemUDF | FsiFileSystemJoliet | FsiFileSystemISO9660)
    );
    if (FAILED(hr)) {
        printf("[-] Failed to set FileSystemsToCreate (0x%x)\n", hr);
    }

    // 获取根目录
    hr = pSystemImage->get_Root(&pRootDirItem);
    if (FAILED(hr)) {
        printf("[-] Failed to get root directory (0x%x)\n", hr);
        pSystemImage->Release();
        return;
    }

    // 将目录树添加到虚拟 ISO
    hr = pRootDirItem->AddTree(CComBSTR(pSrcDir), VARIANT_TRUE);
    if (FAILED(hr)) {
        printf("[-] Failed to AddTree, error (0x%x)\n", hr);
        pRootDirItem->Release();
        pSystemImage->Release();
        return;
    }

    // 生成结果镜像
    hr = pSystemImage->CreateResultImage(&pSystemImageResult);
    if (FAILED(hr)) {
        printf("[-] Failed to CreateResultImage (0x%x)\n", hr);
        pRootDirItem->Release();
        pSystemImage->Release();
        return;
    }

    // 获取生成的镜像数据流
    hr = pSystemImageResult->get_ImageStream(&pImageStream);
    if (FAILED(hr)) {
        printf("[-] Failed to get ImageStream (0x%x)\n", hr);
        pSystemImageResult->Release();
        pRootDirItem->Release();
        pSystemImage->Release();
        return;
    }

    // 创建目标 iso 文件
    HRESULT res = SHCreateStreamOnFileEx(
        pIsoPath,
        STGM_CREATE | STGM_READWRITE,
        FILE_ATTRIBUTE_NORMAL,
        TRUE,
        NULL,
        &pFileStream
    );
    if (FAILED(res)) {
        printf("[-] Failed to create ISO file (0x%x)\n", res);
        pImageStream->Release();
        pSystemImageResult->Release();
        pRootDirItem->Release();
        pSystemImage->Release();
        return;
    }

    // 分块写入拷贝，避免一次性占用超大内存
    STATSTG statstg;
    ULARGE_INTEGER cbSize;
    hr = pImageStream->Stat(&statstg, STATFLAG_DEFAULT);
    if (SUCCEEDED(hr)) {
        cbSize = statstg.cbSize;

        const ULONG bufferSize = 1024 * 1024; // 1 MB 缓冲
        BYTE buffer[bufferSize];
        ULONG cbRead = 0;
        ULONG cbWritten = 0;
        LARGE_INTEGER pos = {};
        pImageStream->Seek(pos, STREAM_SEEK_SET, NULL);

        while (true) {
            hr = pImageStream->Read(buffer, bufferSize, &cbRead);
            if (FAILED(hr) || cbRead == 0)
                break;

            hr = pFileStream->Write(buffer, cbRead, &cbWritten);
            if (FAILED(hr) || cbWritten != cbRead)
                break;
        }

        printf("[+] ISO created successfully: %ls\n", pIsoPath);
    }

    // 释放资源
    pFileStream->Release();
    pImageStream->Release();
    pSystemImageResult->Release();
    pRootDirItem->Release();
    pSystemImage->Release();
}

int _tmain(int argc, TCHAR* argv[])
{
    if (argc != 3) {
        printf("Usage: %ls <source-folder> <output.iso>\n", argv[0]);
        return 1;
    }

    // 判断路径是否存在
    struct stat buffer;
    if (stat((char*)argv[1], &buffer) != 0) {
        printf("[-] Source path doesn't exist: %s\n", argv[1]);
        return 1;
    }

    // 以 Unicode 方式处理参数
    LPWSTR arguments = GetCommandLineW();
    int wArgc;
    LPWSTR* wArgv = CommandLineToArgvW(arguments, &wArgc);
    if (!wArgv) {
        printf("[-] CommandLineToArgvW failed\n");
        return 1;
    }

    LPWSTR pSrc = wArgv[1];
    LPWSTR pIsoPath = wArgv[2];

    CoInitialize(NULL);
    SaveIso(pSrc, pIsoPath);
    CoUninitialize();

    return 0;
}

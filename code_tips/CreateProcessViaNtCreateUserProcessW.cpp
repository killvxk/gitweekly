typedef NTSTATUS(NTAPI* NTCREATEUSERPROCESS)(PHANDLE,PHANDLE, ACCESS_MASK, ACCESS_MASK, POBJECT_ATTRIBUTES, POBJECT_ATTRIBUTES, ULONG, ULONG, PRTL_USER_PROCESS_PARAMETERS, PPS_CREATE_INFO, PPS_ATTRIBUTE_LIST);
typedef NTSTATUS(NTAPI* RTLCREATEPROCESSPARAMETERSEX)(PRTL_USER_PROCESS_PARAMETERS*, PUNICODE_STRING, PUNICODE_STRING, PUNICODE_STRING,	PUNICODE_STRING, PVOID,	PUNICODE_STRING, PUNICODE_STRING, PUNICODE_STRING, PUNICODE_STRING, ULONG);
typedef NTSTATUS(NTAPI* RTLDESTROYPROCESSPARAMETERS)(PRTL_USER_PROCESS_PARAMETERS);

DWORD CreateProcessViaNtCreateUserProcessW(_In_ PWCHAR BinaryPath)
{
	NTCREATEUSERPROCESS NtCreateUserProcess;
	RTLCREATEPROCESSPARAMETERSEX RtlCreateProcessParametersEx;
	RTLDESTROYPROCESSPARAMETERS RtlDestroyProcessParameters;
	PRTL_USER_PROCESS_PARAMETERS ProcessParameters = NULL;
	UNICODE_STRING NtImagePath = {0};
	WCHAR MsDosFullPath[MAX_PATH * sizeof(WCHAR)] = { 0 };
	PS_CREATE_INFO CreateInfo = { 0 };
	HMODULE hModule;
	PPS_ATTRIBUTE_LIST AttributeList = NULL;
	HANDLE hHandle = NULL, hThread = NULL;
	DWORD dwError = ERROR_SUCCESS;

	CreateInfo.Size = sizeof(CreateInfo);
	CreateInfo.State = PsCreateInitialState;

	hModule = GetModuleHandleW(L"ntdll.dll");
	if (hModule == NULL)
		return GetLastErrorFromTeb();

	NtCreateUserProcess = (NTCREATEUSERPROCESS)GetProcAddress(hModule, "NtCreateUserProcess");
	if (NtCreateUserProcess == NULL)
		return GetLastErrorFromTeb();

	RtlCreateProcessParametersEx = (RTLCREATEPROCESSPARAMETERSEX)GetProcAddress(hModule, "RtlCreateProcessParametersEx");
	if (RtlCreateProcessParametersEx == NULL)
		return GetLastErrorFromTeb();

	RtlDestroyProcessParameters = (RTLDESTROYPROCESSPARAMETERS)GetProcAddress(hModule, "RtlDestroyProcessParameters");
	if (RtlDestroyProcessParameters == NULL)
		return GetLastErrorFromTeb();

	StringCopyW(MsDosFullPath, (PWCHAR)L"\\??\\");
	StringConcatW(MsDosFullPath, BinaryPath);

	RtlInitUnicodeString(&NtImagePath, MsDosFullPath);

	if (RtlCreateProcessParametersEx(&ProcessParameters, &NtImagePath, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, RTL_USER_PROCESS_PARAMETERS_NORMALIZED) != ERROR_SUCCESS)
		return GetLastErrorFromTeb();

	AttributeList = (PPS_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeapFromTeb(), HEAP_ZERO_MEMORY, sizeof(PS_ATTRIBUTE));
	if (AttributeList)
	{
		AttributeList->TotalLength = sizeof(PS_ATTRIBUTE_LIST) - sizeof(PS_ATTRIBUTE);
		AttributeList->Attributes[0].Attribute = PS_ATTRIBUTE_IMAGE_NAME;
		AttributeList->Attributes[0].Size = NtImagePath.Length;
		AttributeList->Attributes[0].Value = (ULONG_PTR)NtImagePath.Buffer;

		if (NtCreateUserProcess(&hHandle, &hThread, PROCESS_ALL_ACCESS, THREAD_ALL_ACCESS, NULL, NULL, NULL, NULL, ProcessParameters, &CreateInfo, AttributeList) != ERROR_SUCCESS)
			dwError = GetLastErrorFromTeb(); //?
	}

	if (AttributeList)
		HeapFree(GetProcessHeap(), HEAP_ZERO_MEMORY, AttributeList);

	if (ProcessParameters)
		RtlDestroyProcessParameters(ProcessParameters);

	return dwError;
}

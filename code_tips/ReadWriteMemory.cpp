PVOID CustomCopy(PVOID Destination, CONST PVOID Source, SIZE_T Length)
{
	PBYTE D = (PBYTE)Destination;
	PBYTE S = (PBYTE)Source;

	while (Length--)
		*D++ = *S++;

	return Destination;
}


unsigned char* ReadMemory(LPVOID addrOf, int sizeofVal) 
{
	unsigned char* readBytes = (unsigned char*)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, sizeofVal);
	DWORD dwDataLength = sizeofVal;
	for (DWORD i = 0; i < dwDataLength; i = i + 2)
	{
		HANDLE hThread = NULL;
		NtCreateThreadEx(&hThread, GENERIC_EXECUTE, NULL, NtGetCurrentProcess(), RtlQueryDepthSList, (ULONG_PTR*)((BYTE*)addrOf + i), FALSE, NULL, NULL, NULL, NULL);
		DWORD ExitCode = 0;
		NtWaitForSingleObject(hThread, FALSE, NULL);
		GetExitCodeThread(hThread, &ExitCode);
		if (dwDataLength - i == 1)
		{
			CustomCopy((char*)readBytes + i, (const void*)&ExitCode, 1);
		}
		else
		{
			CustomCopy((char*)readBytes + i, (const void*)&ExitCode, 2);
		}
	}
	return readBytes;
}

void WriteMemory(LPVOID dst, unsigned char* src,int sizeofVal) 
{
  const auto module = GetModuleHandleA("ntdll.dll");
	const auto RtlFillMemory = GetProcAddress(module, "RtlFillMemory");
	const auto RtlExitUserThread = GetProcAddress(module, "RtlExitUserThread");
	const auto RtlInitializeBitMapEx = GetProcAddress(module, "RtlInitializeBitMapEx");
  const auto hProc = NtGetCurrentProcess();

	HANDLE hThread2 = NULL;
	NtCreateThreadEx(&hThread2, THREAD_ALL_ACCESS, NULL, , RtlExitUserThread, (PVOID)0x00000000, TRUE, NULL, NULL, NULL, NULL);
	int alignmentCheck = sizeofVal % 16;
	int offsetMax = sizeofVal - alignmentCheck;
	int firCounter = 0;
	int eightCounter = 0;
	int secCounter = 0;
	int mod = 0;

	if (sizeofVal >= 16) {
		for (firCounter = 0; firCounter < offsetMax -1; firCounter = firCounter + 16) {
			char* heapWriter = (char*)dst + firCounter;
			NtQueueApcThread(hThread2, (PKNORMAL_ROUTINE)RtlInitializeBitMapEx, (PVOID)heapWriter, (PVOID)*(ULONG_PTR*)((char*)src + firCounter + 8), (PVOID)*(ULONG_PTR*)((char*)src + firCounter));
		}
	}

	if (alignmentCheck >= 8) {	
		for (eightCounter = firCounter; (eightCounter + 8) < (firCounter + alignmentCheck -1); eightCounter = eightCounter + 8) {
			char* heapWriter = (char*)dst + eightCounter;
			NtQueueApcThread(hThread2, (PKNORMAL_ROUTINE)RtlInitializeBitMapEx, (PVOID)heapWriter, NULL, (PVOID)*(ULONG_PTR*)((char*)src + eightCounter));
		}
		alignmentCheck -= 8;
	}

	if (alignmentCheck != 0 && alignmentCheck < 8) {

		if ((firCounter != 0 && eightCounter != 0) || (firCounter != 0 && eightCounter != 0)){
			secCounter = eightCounter;
			mod = eightCounter;
		}
		else if (firCounter != 0 && eightCounter == 0){
			secCounter = firCounter;
			mod = firCounter;
		}

		for (; secCounter < (mod + alignmentCheck); secCounter++) {
			char* heapWriter = (char*)dst + secCounter;
			NtQueueApcThread(hThread2, (PKNORMAL_ROUTINE)RtlFillMemory, (PVOID)heapWriter, (PVOID)1, (PVOID)src[secCounter]);
		}
	}

	NtResumeThread(hThread2, NULL);
	NtWaitForSingleObject(hThread2, FALSE, NULL);
}



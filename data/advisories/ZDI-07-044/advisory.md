# ZDI-07-044: BakBone NetVault Reporter Scheduler Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-044
- **ZDI-CAN:** ZDI-CAN-147
- **Date:** 2007-07-25
- **CVE:** CVE-2007-3911
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** BakBone
- **Affected Products:** NetVault Reporter
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with affected installations of BakBone NetVault Reporter. User interaction is not required to exploit this vulnerability. The specific flaw exists both within the scheduler client (clsscheduler.exe) listening on TCP port 7978 and the scheduler server (srvscheduler.exe) listening on TCP port 7977. In both cases an exploitable heap corruption can occur during the processing of overly long filename arguments to the "GET" and "POST" requests. Code execution is possible under the context of the SYSTEM user. When searching for a termination/whitespace character ("\r\t\n") a heap chunk is being used to hold the data. Due to the lack of bounds checking on this heap chunk an overflow occurs when a long string without any of the above special characters are encountered. The vulnerable code appears below. 0x00466C07 mov al, [esi+ebp] 0x00466C0A cmp al, 20h 0x00466C0C jz short loc_466C84 0x00466C0E cmp al, 9 0x00466C10 jz short loc_466C84 0x00466C12 cmp al, 0Ah 0x00466C14 jz short loc_466C84 0x00466C16 cmp al, 0Dh 0x00466C18 jz short loc_466C84 0x00466C1A push 1 0x00466C1C inc esi 0x00466C1D push 1 0x00466C1F lea edx, [esi+ebp] ; heap chunk 0x00466C22 push edx ; readfds 0x00466C23 mov ecx, edi 0x00466C25 call sub_4645C0 ; recv 1 byte 0x00466C2A cmp eax, 0FFFFFFFFh 0x00466C2D mov [ebx+272Ch], eax 0x00466C33 jnz short loc_466C07 ;loop

## Additional Details

BakBone has issued an update to correct this vulnerability. More details can be found at: http://www.bakbone.com/products/downloads/default.asp

## Disclosure Timeline

- 2007-02-23 - Vulnerability reported to vendor
- 2007-07-25 - Coordinated public release of advisory

# ZDI-11-026: Novell Zenworks Handheld Management ZfHIPCnd.exe Opcode 2 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-026
- **ZDI-CAN:** ZDI-CAN-1071
- **Date:** 2011-01-26
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks Handheld Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Access Point process (ZfHIPCnd.exe) which listens by default on TCP port 2400. The problem occurs due to the application copying arbitrary sized data from a packet into a statically sized buffer. Due to the application not accommodating for the variable sized data during initialization of this buffer a buffer overflow will occur. This can lead to code execution under the context of the application.

## Additional Details

TID 7007663: http://www.novell.com/support/dynamickc.do?cmd=show&forward=nonthreadedKC&docType=kc&externalId=7007663&sliceId=1 Patch: http://download.novell.com/Download?buildid=x_x4cdA5yT8~

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-01-26 - Coordinated public release of advisory

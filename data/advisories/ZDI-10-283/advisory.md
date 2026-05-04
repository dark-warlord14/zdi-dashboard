# ZDI-10-283: Novell ZENWorks Remote Management Agent Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-283
- **ZDI-CAN:** ZDI-CAN-749
- **Date:** 2010-12-13
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** sb
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-283/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENWorks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ZenRem32.exe process which listens by default on TCP and UDP ports 1761. When processing incoming connections with specific version fields the process fails to initialize a string buffer intended to hold the name of the client. After making allocations based on the size of the uninitialized string, ZenRem32 proceeds to convert the buffer between wide-char and multi-byte data types. As the pointer is directed at uninitialized memory, this can be abused to corrupt the heap. An attacker can leverage this to execute remote code under the context of the SYSTEM user.

## Additional Details

Fixed in ZENworks 7 Desktop Management Support Pack 1 Interim Release 4 Hot Patch 5: http://download.novell.com/Download?buildid=r9kcCymJ7Os Documented in TID 7007320 http://www.novell.com/support/dynamickc.do?cmd=show&forward=nonthreadedKC&docType=kc&externalId=7007320&sliceId=1

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-12-13 - Coordinated public release of advisory

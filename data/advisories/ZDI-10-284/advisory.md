# ZDI-10-284: Novell ZENWorks Remote Management Agent DN Name Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-284
- **ZDI-CAN:** ZDI-CAN-751
- **Date:** 2010-12-13
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** sb
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-284/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENWorks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ZenRem32.exe process which listens by default on TCP and UDP ports 1761. When processing the Console DN field of incoming requests, the process can be made to overflow a stack buffer by 2 bytes. Due to the location of the destination buffer, an attacker can abuse this to overwrite a portion of a return address and execute remote code under the context of the SYSTEM user.

## Additional Details

Fixed in ZENworks 7 Desktop Management Support Pack 1 Interim Release 4 Hot Patch 5: http://download.novell.com/Download?buildid=r9kcCymJ7Os Documented in TID 7007339 http://www.novell.com/support/dynamickc.do?cmd=show&forward=nonthreadedKC&docType=kc&externalId=7007339&sliceId=1

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-12-13 - Coordinated public release of advisory

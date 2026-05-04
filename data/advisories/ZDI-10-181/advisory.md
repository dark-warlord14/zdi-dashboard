# ZDI-10-181: IBM TSM FastBack Server ActivateLTScriptReply Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-181
- **ZDI-CAN:** ZDI-CAN-660
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli FastBack Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe which listens by default on tcp port 11406. The issue is due to a memcpy within the _AGI_S_ActivateLTScriptReply function. The process trusts a user-supplied length and copies user-supplied data to a fixed length buffer located on the stack. Successful exploitation leads to remote code execution under the context of the fastback server.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 2

## Disclosure Timeline

- 2010-01-22 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory

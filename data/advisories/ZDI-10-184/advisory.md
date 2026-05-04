# ZDI-10-184: IBM TSM FastBack Server USER_S_AddADGroup Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-184
- **ZDI-CAN:** ZDI-CAN-663
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-184/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli FastBack Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe which listens by default on TCP port 11460. The issue is due to a strcat of user supplied data to a fixed length buffer located on the stack. By providing sufficiently large values for a group, workgroup, or domain name this buffer can be overflowed. Successful exploitation leads to remote code execution under the context of the fastback server.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 2

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory

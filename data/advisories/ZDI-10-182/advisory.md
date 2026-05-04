# ZDI-10-182: IBM TSM FastBack Server FXCLI_OraBR_Exec_Command Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-182
- **ZDI-CAN:** ZDI-CAN-661
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Sebastian Apelt (www.siberas.de) Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli FastBack Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe which listens by default on TCP port 11460. The vulnerable function uses values directly from a received packet as the size and data to several memcpy calls. By providing crafted values this issue can lead to remote code execution under the context of the fastback server.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 2

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory

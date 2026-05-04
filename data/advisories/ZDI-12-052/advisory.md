# ZDI-12-052: FlexNet License Server Manager lmgrd Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-052
- **ZDI-CAN:** ZDI-CAN-1192
- **Date:** 2012-03-26
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Flexera Software
- **Affected Products:** FlexNet License Server Manager
- **Credit:** Luigi Auriemma Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of FlexNet License Server Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within lmgrd license server manager. lmgrd listens by default on TCP port 27000. A specially crafted packet sent to the server will cause a stack overflow allowing for remote code execution under the context of the server.

## Additional Details

Flexera Software has issued an update to correct this vulnerability. More details can be found at: http://www.flexerasoftware.com/pl/13057.htm

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2012-03-26 - Coordinated public release of advisory

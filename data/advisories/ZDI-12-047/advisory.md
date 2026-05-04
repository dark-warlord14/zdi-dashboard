# ZDI-12-047: Adobe Flash ASconstructor Function Call Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-047
- **ZDI-CAN:** ZDI-CAN-1362
- **Date:** 2012-03-22
- **CVE:** CVE-2012-0754
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Adobe Flash player handles calls to the _global.ASconstructor function. If this function is called with id '2200' it will write a 0x01 byte to a user supplied address. This memory corruption can result in remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb12-03.html

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-03-22 - Coordinated public release of advisory

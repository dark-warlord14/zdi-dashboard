# ZDI-10-278: RealNetworks RealPlayer Custsupport.html Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-278
- **ZDI-CAN:** ZDI-CAN-845
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4388
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-278/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Custsupport.html component of the RealPlayer default installation. Due to a failure to properly sanitize user-supplied input, it is possible for an attacker to inject arbitrary code into the RealOneActiveXObject process. This can be abused to bypass the Local Machine Zone security policy and load unsafe controls. Successful exploitation of this issue leads to remote code execution under the context of the RealPlayer application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

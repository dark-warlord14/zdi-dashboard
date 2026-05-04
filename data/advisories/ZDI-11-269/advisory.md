# ZDI-11-269: RealNetworks RealPlayer Cross-Zone Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-269
- **ZDI-CAN:** ZDI-CAN-1152
- **Date:** 2011-08-16
- **CVE:** CVE-2011-2947
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Martin Bartek
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to the fact that RealPlayer allows users to run local HTML files with scripting enabled without any warning. The RealPlayer ActiveX control can be scripted from a web browser to load local HTML files. This can lead to remote code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08162011_player/en/

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory

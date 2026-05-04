# ZDI-11-268: RealNetworks RealPlayer SWF DefineFont Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-268
- **ZDI-CAN:** ZDI-CAN-1185
- **Date:** 2011-08-16
- **CVE:** CVE-2011-2948
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-268/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way RealPlayer handles DEFINEFONT fields in Flash Files. When the process parses corrupt a ShapeRecord with the DefineFont record it reads outside a stack buffer and uses a random stack value as a heap pointer. Later this pointer will be used to write data into. The resulting corruption can lead to remote code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08162011_player/en/

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory

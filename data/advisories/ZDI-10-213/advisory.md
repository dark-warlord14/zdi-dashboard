# ZDI-10-213: RealNetworks RealPlayer Multiple Protocol Handlers Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-213
- **ZDI-CAN:** ZDI-CAN-724
- **Date:** 2010-10-15
- **CVE:** CVE-2010-3751
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-213/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the RealPlayer ActiveX control. This module is responsible for handling the tfile, pnmm, cdda, protocol handlers. While parsing a long argument ending with ".smil" an attacker can overflow a buffer on the heap. This can be abused to execute arbitrary code under the context of the user invoking the control.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10152010_player/en/

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2010-10-15 - Coordinated public release of advisory

# ZDI-10-007: RealNetworks RealPlayer SMIL getAtom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-007
- **ZDI-CAN:** ZDI-CAN-286
- **Date:** 2010-01-21
- **CVE:** CVE-2009-4257
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-007/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the smlrender.dll library responsible for parsing SMIL files. A lack of proper string length checks can result in the overflow of a static heap buffer. Exploitation of this overflow can lead to arbitrary code execution under the context of the user running the process.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/01192010_player/en/

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory

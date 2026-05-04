# ZDI-10-212: RealNetworks RealPlayer RJMDSections Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-212
- **ZDI-CAN:** ZDI-CAN-677
- **Date:** 2010-10-15
- **CVE:** CVE-2010-3750
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-212/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a target must open a malicious website or media file. The specific flaw exists within the code responsible for parsing Name Value Property (NVP) elements from within logical streams in a RealPlayer media file. Specifically, a function within the rjrmrpln.dll file allocates a buffer on the heap which can be directly influenced from data within the file. This buffer is then written to using another value defined in the file and thus also controlled. By crafting a malicious media file an attacker can abuse this to execute arbitrary code under the context of the user running the player.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10152010_player/en/

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-10-15 - Coordinated public release of advisory

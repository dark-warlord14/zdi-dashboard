# ZDI-10-006: RealNetworks RealPlayer GIF Handling Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-006
- **ZDI-CAN:** ZDI-CAN-271
- **Date:** 2010-01-21
- **CVE:** CVE-2009-4242
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-006/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a user must open a malicious file or visit a malicious web site. The specific flaw exists during the parsing of GIF files with forged chunk sizes. The player uses values from the file improperly when allocating a buffer on the heap. An attacker can abuse this to create and then overflow heap buffers leading to arbitrary code execution in the context of the currently logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/01192010_player/en/

## Disclosure Timeline

- 2007-12-11 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory

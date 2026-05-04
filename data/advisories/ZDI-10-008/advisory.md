# ZDI-10-008: RealNetworks RealPlayer SIPR Codec Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-008
- **ZDI-CAN:** ZDI-CAN-317
- **Date:** 2010-01-21
- **CVE:** CVE-2009-4244
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a user must open a malicious file or visit a malicious web site. The specific flaw exists during the parsing of SIPR codec fields. Specifying a small length value can trigger an undersized heap allocation. This buffer can then subsequently be overflowed. This vulnerability can result in arbitrary code execution under the context of the currently logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/01192010_player/en/

## Disclosure Timeline

- 2008-05-12 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory

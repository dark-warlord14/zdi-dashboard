# ZDI-10-268: RealNetworks RealPlayer Media Properties Header Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-268
- **ZDI-CAN:** ZDI-CAN-434
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4384
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous Hossein Lotfi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-268/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when parsing a RealMedia file containing a malformed Media Properties Header (MDPR). The application explicitly trusts an index in this data structure which is used to seek into an array of objects. If an attacker can allocate controlled data at some point after this array, an attacker can then get their fabricated object to get called leading to code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2009-02-24 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

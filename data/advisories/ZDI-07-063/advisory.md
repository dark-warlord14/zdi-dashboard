# ZDI-07-063: RealPlayer RA Field Size File Processing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-063
- **ZDI-CAN:** ZDI-CAN-150
- **Date:** 2007-10-31
- **CVE:** CVE-2007-2264
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-063/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealPlayer. User interaction is required in that a user must open a malicious .ra/.ram file or visit a malicious web site. The specific flaw exists during the parsing of files with improperly defined size field in the RA header. Specifying a large unsigned value data can trigger a heap corruption and further result in arbitrary code execution under the context of the logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10252007_player/en/

## Disclosure Timeline

- 2007-02-16 - Vulnerability reported to vendor
- 2007-10-31 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated

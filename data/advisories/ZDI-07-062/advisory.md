# ZDI-07-062: RealNetworks RealPlayer PLS File Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-062
- **ZDI-CAN:** ZDI-CAN-148
- **Date:** 2007-10-31
- **CVE:** CVE-2007-4599
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealPlayer. User interaction is required in that a user must open a malicious .pls file or visit a malicious web site. The specific flaw exists during the parsing of corrupted playlist files. Malicious corruption causes RealPlayer to call into a static heap address which can be leveraged by an attacker resulting in arbitrary code execution under the context of the logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10252007_player/en/

## Disclosure Timeline

- 2007-03-09 - Vulnerability reported to vendor
- 2007-10-31 - Coordinated public release of advisory

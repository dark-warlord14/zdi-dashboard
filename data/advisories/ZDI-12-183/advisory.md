# ZDI-12-183: RealNetworks RealPlayer RV40 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-183
- **ZDI-CAN:** ZDI-CAN-1191
- **Date:** 2012-11-15
- **CVE:** CVE-2012-0925
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Dan Rosenberg of Virtual Security Research Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-183/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a target must visit a malicious page or open a malicious file. The flaw exists within the rv40.dll component for RealNetworks RealPlayer. When parsing a stream containing RV40 sample data, a value is miscalculated before being used as an offset from a base pointer address. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/09072012_player/en/

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-11-15 - Coordinated public release of advisory

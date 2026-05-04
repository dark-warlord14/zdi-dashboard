# ZDI-12-084: RealNetworks RealPlayer RV10 Encoded Height/Width Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-084
- **ZDI-CAN:** ZDI-CAN-1293
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0926
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Dan Rosenberg of Virtual Security Research Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a target must visit a malicious page or open a malicious file. The flaw exists within the RV10 encoded data in the rv10.dll component. When encountering an invalid encoded height or width field the process miscalculates an offset while preparing to decode the data packets which constitute the stream. The process attempts to store data at this location. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/02062012_player/en/

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory

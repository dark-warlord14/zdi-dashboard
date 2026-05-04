# ZDI-25-628: (Pwn2Own) Phoenix Contact CHARX SEC-3150 OCPP Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-628
- **ZDI-CAN:** ZDI-CAN-26346
- **Date:** 2025-07-22
- **CVE:** CVE-2025-25271
- **CVSS:** 3.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3150
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-628/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Phoenix Contact CHARX SEC-3150 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the OCPP service. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://certvde.com/en/advisories/VDE-2025-019/

## Disclosure Timeline

- 2025-03-04 - Vulnerability reported to vendor
- 2025-07-22 - Coordinated public release of advisory
- 2025-07-22 - Advisory Updated

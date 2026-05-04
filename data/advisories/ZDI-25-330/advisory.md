# ZDI-25-330: (0Day) (Pwn2Own) WOLFBOX Level 2 EV Charger Management Card Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-330
- **ZDI-CAN:** ZDI-CAN-26292
- **Date:** 2025-06-06
- **CVE:** CVE-2025-5751
- **CVSS:** 4.6
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** WOLFBOX
- **Affected Products:** Level 2 EV Charger
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-330/
## Vulnerability Details

This vulnerability allows physically present attackers to bypass authentication on affected installations of WOLFBOX Level 2 EV Charger. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of management cards. The issue results from the lack of personalization of management cards. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

ZDI made several attempts to contact the vendor using the contact information on their website, as well as trying to reach them on various social platforms which yielded no response. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-06-06 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated

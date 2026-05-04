# ZDI-25-342: (Pwn2Own) Autel MaxiCharger AC Wallbox Commercial PIN Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-342
- **ZDI-CAN:** ZDI-CAN-26352
- **Date:** 2025-06-11
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Autel
- **Affected Products:** Autel MaxiCharger AC Wallbox Commercial
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-342/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Autel MaxiCharger AC Wallbox Commercial charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Pile API. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose credentials, leading to further compromise.

## Additional Details

Fixed in American Standard: V1.39.51 and European Standard: V1.56.51

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

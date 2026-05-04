# ZDI-25-340: (Pwn2Own) Autel MaxiCharger AC Wallbox Commercial Technician API Incorrect Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-340
- **ZDI-CAN:** ZDI-CAN-26325
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5822
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Autel
- **Affected Products:** Autel MaxiCharger AC Wallbox Commercial
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-340/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Autel MaxiCharger AC Wallbox Commercial charging stations. An attacker must first obtain a low-privileged authorization token in order to exploit this vulnerability. The specific flaw exists within the implementation of the Autel Technician API. The issue results from incorrect authorization. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Fixed in American Standard: V1.39.51 and European Standard: V1.56.51

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

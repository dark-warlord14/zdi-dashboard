# ZDI-23-1103: Schneider Electric IGSS UpdateService Exposed Dangerous Method Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1103
- **ZDI-CAN:** ZDI-CAN-20851
- **Date:** 2023-08-14
- **CVE:** CVE-2023-3001
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1103/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric IGSS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of commands by the UpdateService service. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-220-01

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2023-08-14 - Coordinated public release of advisory

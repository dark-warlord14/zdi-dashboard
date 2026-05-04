# ZDI-24-520: (Pwn2Own) Phoenix Contact CHARX SEC-3100 Missing Encryption Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-520
- **ZDI-CAN:** ZDI-CAN-23418
- **Date:** 2024-05-29
- **CVE:** CVE-2024-28134
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-520/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of nginx. The issue results from a lack of encryption. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the user-app account.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-019/

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

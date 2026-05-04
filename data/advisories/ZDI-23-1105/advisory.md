# ZDI-23-1105: CODESYS Development System Improper Enforcement of Message Integrity Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1105
- **ZDI-CAN:** ZDI-CAN-20816
- **Date:** 2023-08-14
- **CVE:** CVE-2023-3663
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** CODESYS
- **Affected Products:** Development System
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1105/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of CODESYS Development System. Authentication is not required to exploit this vulnerability. The specific flaw exists within the LearnMoreAction function. The issue results from a missing integrity check on notification data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

https://cert.vde.com/en/advisories/VDE-2023-022/ https://customers.codesys.com/index.php?eID=dumpFile&t=f&f=17767&token=7ed2d9324eff98a0a319c455d0256dc7627c705e&download=

## Disclosure Timeline

- 2023-05-11 - Vulnerability reported to vendor
- 2023-08-14 - Coordinated public release of advisory

# ZDI-24-1223: Ivanti Endpoint Manager AgentPortal Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1223
- **ZDI-CAN:** ZDI-CAN-23850
- **Date:** 2024-09-12
- **CVE:** CVE-2024-29847
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1223/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AgentPortal service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-September-2024-for-EPM-2024-and-EPM-2022?language=en_US

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-09-12 - Coordinated public release of advisory
- 2024-09-12 - Advisory Updated

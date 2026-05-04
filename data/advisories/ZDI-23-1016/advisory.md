# ZDI-23-1016: CODESYS Development System Exposure of Resource to Wrong Sphere Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1016
- **ZDI-CAN:** ZDI-CAN-20295
- **Date:** 2023-08-03
- **CVE:** CVE-2023-3670
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** CODESYS
- **Affected Products:** Development System
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1016/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of CODESYS Development System. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of python scripts. The issue results from the lack of resource separation between control spheres. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the Administrator.

## Additional Details

CODESYS has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2023-024/

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-08-03 - Coordinated public release of advisory

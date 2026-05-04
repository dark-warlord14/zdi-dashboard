# ZDI-24-1222: Ivanti Workspace Control RES Exposed Dangerous Method Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1222
- **ZDI-CAN:** ZDI-CAN-23860
- **Date:** 2024-09-11
- **CVE:** CVE-2024-8012
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Workspace Control
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1222/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Ivanti Workspace Control. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the RES service, which listens on TCP port 1942 by default. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Workspace-Control-IWC

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-09-11 - Coordinated public release of advisory
- 2024-09-11 - Advisory Updated

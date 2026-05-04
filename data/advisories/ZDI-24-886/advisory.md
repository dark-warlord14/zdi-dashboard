# ZDI-24-886: Progress Software WhatsUp Gold SetAdminPassword Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-886
- **ZDI-CAN:** ZDI-CAN-24004
- **Date:** 2024-07-03
- **CVE:** CVE-2024-5009
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-886/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Progress Software WhatsUp Gold. An attacker must first obtain the ability to execute low-privileged code on the target system or send an HTTP request from a local machine in order to exploit this vulnerability. The specific flaw exists within the implementation of SetAdminPassword method. The issue results from the improper access control. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-June-2024

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

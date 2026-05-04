# ZDI-24-1187: Progress Software WhatsUp Gold getMonitorJoin SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1187
- **ZDI-CAN:** ZDI-CAN-23667
- **Date:** 2024-08-29
- **CVE:** CVE-2024-6672
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1187/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Progress Software WhatsUp Gold. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the getMonitorJoin method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2024

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-08-29 - Coordinated public release of advisory
- 2024-08-29 - Advisory Updated

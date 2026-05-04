# ZDI-24-1186: Progress Software WhatsUp Gold GetStatisticalMonitorList SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1186
- **ZDI-CAN:** ZDI-CAN-23662
- **Date:** 2024-08-29
- **CVE:** CVE-2024-6671
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1186/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Progress Software WhatsUp Gold. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of GetStatisticalMonitorList method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2024

## Disclosure Timeline

- 2024-05-22 - Vulnerability reported to vendor
- 2024-08-29 - Coordinated public release of advisory
- 2024-08-29 - Advisory Updated

# ZDI-24-1687: Progress Software WhatsUp Gold GetFilterCriteria SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1687
- **ZDI-CAN:** ZDI-CAN-24647
- **Date:** 2024-12-12
- **CVE:** CVE-2024-46908
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1687/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Progress Software WhatsUp Gold. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the GetFilterCriteria method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://www.cve.org/CVERecord?id=CVE-2024-46908

## Disclosure Timeline

- 2024-08-14 - Vulnerability reported to vendor
- 2024-12-12 - Coordinated public release of advisory
- 2024-12-12 - Advisory Updated

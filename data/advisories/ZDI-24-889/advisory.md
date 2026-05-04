# ZDI-24-889: Progress Software WhatsUp Gold InstallController Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-889
- **ZDI-CAN:** ZDI-CAN-23869
- **Date:** 2024-07-03
- **CVE:** CVE-2024-5013
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-889/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Progress Software WhatsUp Gold. Authentication is not required to exploit this vulnerability. The specific flaw exists within the InstallController class. The issue results from the lack of validating the current installation step. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-June-2024

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

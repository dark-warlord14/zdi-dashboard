# ZDI-24-888: Progress Software WhatsUp Gold Missing Authentication GetWindowsCredential Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-888
- **ZDI-CAN:** ZDI-CAN-23659
- **Date:** 2024-07-03
- **CVE:** CVE-2024-5015
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-888/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Progress Software WhatsUp Gold. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GetWindowsCredential method. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-June-2024

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

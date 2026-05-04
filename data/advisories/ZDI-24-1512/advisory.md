# ZDI-24-1512: Progress Software WhatsUp Gold getReport Missing Authentication Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1512
- **ZDI-CAN:** ZDI-CAN-23661
- **Date:** 2024-11-18
- **CVE:** CVE-2024-7763
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1512/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Progress Software WhatsUp Gold. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of getReport method. The issue results from the lack of authentication and authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2024

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-11-18 - Coordinated public release of advisory
- 2024-11-18 - Advisory Updated

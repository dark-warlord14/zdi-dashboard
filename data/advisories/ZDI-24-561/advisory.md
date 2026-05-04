# ZDI-24-561: Progress Software Telerik Reporting Register Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-561
- **ZDI-CAN:** ZDI-CAN-23879
- **Date:** 2024-05-31
- **CVE:** CVE-2024-4358
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** Telerik Reporting
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-561/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Progress Software Telerik Reporting. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the Register method. The issue results from the lack of validating the current installation step. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.telerik.com/report-server/knowledge-base/registration-auth-bypass-cve-2024-4358

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

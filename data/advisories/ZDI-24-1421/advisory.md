# ZDI-24-1421: VMware HCX listExtensions SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1421
- **ZDI-CAN:** ZDI-CAN-23941
- **Date:** 2024-10-23
- **CVE:** CVE-2024-38814
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** VMware HCX
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1421/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware HCX. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the listExtensions method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the postgres user.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25019

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-10-23 - Coordinated public release of advisory
- 2024-10-23 - Advisory Updated

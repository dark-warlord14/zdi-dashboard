# ZDI-24-364: Arista NG Firewall ReportEntry SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-364
- **ZDI-CAN:** ZDI-CAN-21954
- **Date:** 2024-04-09
- **CVE:** CVE-2024-27889
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Gereon Huppertz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-364/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Arista NG Firewall. Authentication is required to exploit this vulnerability. The specific flaw exists within the ReportEntry class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the postgres user.

## Additional Details

Arista has issued an update to correct this vulnerability. More details can be found at: https://www.arista.com/en/support/advisories-notices/security-advisory/19038-security-advisory-0093

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2024-04-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

# ZDI-24-899: Centreon testServiceExistence SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-899
- **ZDI-CAN:** ZDI-CAN-23078
- **Date:** 2024-07-15
- **CVE:** CVE-2024-39841
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** cchav3z
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-899/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the testServiceExistence function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the apache user.

## Additional Details

Fixed in centreon-web versions: 22.04.24, 22.10.22, 23.04.18, 23.10.12, 24.04.3

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-07-15 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

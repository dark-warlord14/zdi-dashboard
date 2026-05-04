# ZDI-24-113: Centreon insertGraphTemplate SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-113
- **ZDI-CAN:** ZDI-CAN-22339
- **Date:** 2024-02-09
- **CVE:** CVE-2024-23119
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** 129cf345fa3dcf0fd346682161ba9a4f
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the insertGraphTemplate function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in Centreon-web versions 22.10.15, 23.04.10 and 23.10.1 https://github.com/centreon/centreon/pull/2464

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

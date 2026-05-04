# ZDI-22-954: Centreon Virtual Metrics SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-954
- **ZDI-CAN:** ZDI-CAN-16336
- **Date:** 2022-07-07
- **CVE:** CVE-2022-34872
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-954/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of Virtual Metrics. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Centreon has issued an update to correct this vulnerability. More details can be found at: https://docs.centreon.com/docs/21.10/releases/centreon-core/

## Disclosure Timeline

- 2022-02-16 - Vulnerability reported to vendor
- 2022-07-07 - Coordinated public release of advisory
- 2022-08-03 - Advisory Updated

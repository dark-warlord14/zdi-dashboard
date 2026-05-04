# ZDI-23-1500: Cacti graph_view SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1500
- **ZDI-CAN:** ZDI-CAN-20767
- **Date:** 2023-10-04
- **CVE:** CVE-2023-39365
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cacti
- **Affected Products:** Cacti
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1500/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication or escalate privileges on affected installations of Cacti. Authentication is required to exploit this vulnerability when the product is in its default configuration. The specific flaw exists within the graph_view endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Cacti has issued an update to correct this vulnerability. More details can be found at: https://github.com/cacti/cacti/security/advisories/GHSA-v5w7-hww7-2f22

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory

# ZDI-25-852: (0Day) CData API Server MySQL Misconfiguration Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-852
- **ZDI-CAN:** ZDI-CAN-23950
- **Date:** 2025-08-20
- **CVE:** CVE-2025-9273
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** CData
- **Affected Products:** API Server
- **Credit:** adhkr - LuwakLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-852/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of CData API Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the usage of MySQL connections. When connecting to a MySQL server, the product enables an option that gives the MySQL server permission to request local files from the MySQL client. An attacker can leverage this vulnerability to disclose information in the context of NETWORK SERVICE.

## Additional Details

11/13/24 - ZDI reported the vulnerability to the vendor 03/09/25 - ZDI asked for updates 08/08/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-11-13 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-08-20 - Advisory Updated

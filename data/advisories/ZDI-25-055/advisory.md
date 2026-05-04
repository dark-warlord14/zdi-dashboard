# ZDI-25-055: Sante PACS Server URL path Memory Corruption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-055
- **ZDI-CAN:** ZDI-CAN-25318
- **Date:** 2025-01-20
- **CVE:** CVE-2025-0574
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server
- **Credit:** Chizuru Toyama of TXOne Networks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-055/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Sante PACS Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of URLs in the web server module. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in Sante PACS Server version 4.0.10

## Disclosure Timeline

- 2024-09-13 - Vulnerability reported to vendor
- 2025-01-20 - Coordinated public release of advisory
- 2025-01-20 - Advisory Updated

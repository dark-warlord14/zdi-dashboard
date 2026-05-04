# ZDI-25-1104: Sante PACS Server HTTP Content-Length Header Handling NULL Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1104
- **ZDI-CAN:** ZDI-CAN-26770
- **Date:** 2025-12-17
- **CVE:** CVE-2025-14501
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server
- **Credit:** Artur Mattern
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1104/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Sante PACS Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP Content-Length header. The issue results from the lack of proper validation of a pointer prior to accessing it. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in version 4.2.3

## Disclosure Timeline

- 2025-06-12 - Vulnerability reported to vendor
- 2025-12-17 - Coordinated public release of advisory
- 2025-12-17 - Advisory Updated

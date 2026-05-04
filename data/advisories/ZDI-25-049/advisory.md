# ZDI-25-049: Sante PACS Server DCM File Parsing Memory Corruption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-049
- **ZDI-CAN:** ZDI-CAN-25302
- **Date:** 2025-01-20
- **CVE:** CVE-2025-0568
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server
- **Credit:** Chizuru Toyama of TXOne Networks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-049/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Sante PACS Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of DCM files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in Sante PACS Server version 4.0.10

## Disclosure Timeline

- 2024-09-03 - Vulnerability reported to vendor
- 2025-01-20 - Coordinated public release of advisory
- 2025-01-20 - Advisory Updated

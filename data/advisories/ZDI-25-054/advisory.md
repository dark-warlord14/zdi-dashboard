# ZDI-25-054: Sante PACS Server Web Portal DCM File Parsing Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-054
- **ZDI-CAN:** ZDI-CAN-25308
- **Date:** 2025-01-20
- **CVE:** CVE-2025-0572
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server
- **Credit:** Chizuru Toyama of TXOne Networks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-054/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Sante PACS Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the parsing of DCM files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to write files in the context of the current user.

## Additional Details

Fixed in Sante PACS Server version 4.0.10

## Disclosure Timeline

- 2024-09-10 - Vulnerability reported to vendor
- 2025-01-20 - Coordinated public release of advisory
- 2025-01-20 - Advisory Updated

# ZDI-22-1032: EnterpriseDT CompleteFTP Server HttpFile Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1032
- **ZDI-CAN:** ZDI-CAN-17481
- **Date:** 2022-07-28
- **CVE:** CVE-2022-2560
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** EnterpriseDT
- **Affected Products:** CompleteFTP
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1032/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of EnterpriseDT CompleteFTP Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HttpFile class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Fixed in version 22.1.1.

## Disclosure Timeline

- 2022-06-07 - Vulnerability reported to vendor
- 2022-07-28 - Coordinated public release of advisory

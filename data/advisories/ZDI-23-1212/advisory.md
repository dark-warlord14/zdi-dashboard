# ZDI-23-1212: (0Day) LG Simple Editor putCanvasDB Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1212
- **ZDI-CAN:** ZDI-CAN-20010
- **Date:** 2023-08-24
- **CVE:** CVE-2023-40508
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** LG
- **Affected Products:** Simple Editor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1212/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of LG Simple Editor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the putCanvasDB method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

02/13/23 – The ZDI requested a vendor PSIRT contact. 02/14/23 – The vendor provided PSIRT Contact information. 02/14/23 – The ZDI reported the vulnerability to the vendor. 08/04/23 – The ZDI asked for an update. 08/08/23 – The vendor states that they do not have plans to fix the vulnerability now or in the future. 08/21/23 – The ZDI informed the vendor that we are publishing the case as a zero-day advisory on 08/24/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-14 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory

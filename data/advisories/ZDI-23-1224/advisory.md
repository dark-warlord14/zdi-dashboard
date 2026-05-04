# ZDI-23-1224: LG LED Assistant updateFile Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1224
- **ZDI-CAN:** ZDI-CAN-20270
- **Date:** 2023-08-25
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** LG
- **Affected Products:** LED Assistant
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1224/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of LG LED Assistant. Authentication is not required to exploit this vulnerability. The specific flaw exists within the /api/download/updateFile endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

LG has issued an update to correct this vulnerability. More details can be found at: https://lgsecurity.lge.com/bulletins/idproducts#updateDetails

## Disclosure Timeline

- 2023-03-10 - Vulnerability reported to vendor
- 2023-08-25 - Coordinated public release of advisory

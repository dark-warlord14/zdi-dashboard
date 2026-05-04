# ZDI-23-1401: ManageEngine ADManager Plus download Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1401
- **ZDI-CAN:** ZDI-CAN-21184
- **Date:** 2023-09-11
- **CVE:** CVE-2023-39912
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** ManageEngine
- **Affected Products:** ADManager Plus
- **Credit:** Son Nguyen from VNG Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1401/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ManageEngine ADManager Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the download method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/ad-manager/admanager-kb/cve-2023-39912.html

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-09-11 - Coordinated public release of advisory

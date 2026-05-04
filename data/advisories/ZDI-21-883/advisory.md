# ZDI-21-883: Oracle Business Intelligence UploadFndDBCPage Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-883
- **ZDI-CAN:** ZDI-CAN-13377
- **Date:** 2021-07-22
- **CVE:** CVE-2021-2392
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** kpc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-883/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Business Intelligence. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the UploadFndDBCPage class. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2021.html

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory

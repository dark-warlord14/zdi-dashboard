# ZDI-11-352: HP Managed Printing Administration jobAcct Multiple Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-11-352
- **ZDI-CAN:** ZDI-CAN-1064
- **Date:** 2011-12-22
- **CVE:** CVE-2011-4166
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Managed Printing Administration
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-352/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Managed Printing Administration. Authentication is not required to exploit this vulnerability. There multiple classes of flaws within this product including arbitrary file creation, null char truncation and directory traversal. Null injection and directory traversal can be used in the form data passed to MPAUploader.Uploader.1.UploadFiles() to remotely create arbitrary files.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128469

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-12-22 - Coordinated public release of advisory

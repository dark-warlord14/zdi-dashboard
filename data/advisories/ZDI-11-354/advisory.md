# ZDI-11-354: HP Managed Printing Administration jobDelivery Multiple Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-11-354
- **ZDI-CAN:** ZDI-CAN-1066
- **Date:** 2011-12-22
- **CVE:** CVE-2011-4168
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Managed Printing Administration
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-354/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Managed Printing Administration. Authentication is not required to exploit this vulnerability. There multiple classes of flaws within this product including arbitrary file creation, null char truncation and directory traversal. Null injection and directory traversal can be used in the form data passed to \Inetpub\wwwroot\hpmpa\jobDelivery\Default.asp to remotely create arbitrary files.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128469

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-12-22 - Coordinated public release of advisory

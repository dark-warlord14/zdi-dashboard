# ZDI-12-001: HP Managed Printing Administration img_id Multiple Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-12-001
- **ZDI-CAN:** ZDI-CAN-1067
- **Date:** 2012-01-05
- **CVE:** CVE-2011-4169
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Managed Printing Administration
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-001/
## Vulnerability Details

This vulnerability allows remote attackers to remotely manipulate the application database and delete arbitrary files on vulnerable installations of HP Managed Printing Administration. Authentication is not required to exploit this vulnerability. The specific flaw exists and is duplicated within the following scripts: \Inetpub\wwwroot\hpmpa\mpl\view\config\imglist\imgselect\Default.asp \Inetpub\wwwroot\hpmpa\mpl\view\config\imgmap\bgselect\Default.asp \Inetpub\wwwroot\hpmpa\mpl\view\config\imgmap\imgselect\Default.asp Input via the img_id parameter to the aforementioned scripts can be manipulated to perform SQL injection. Additionally, directory traversal can be used on this parameter to delete arbitrary files.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128469

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2012-01-05 - Coordinated public release of advisory

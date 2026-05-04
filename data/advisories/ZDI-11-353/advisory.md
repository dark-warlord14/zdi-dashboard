# ZDI-11-353: HP Managed Printing Administration MPAUploader.dll Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-353
- **ZDI-CAN:** ZDI-CAN-1065
- **Date:** 2011-12-22
- **CVE:** CVE-2011-4167
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Managed Printing Administration
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-353/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Managed Printing Administration. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MPAUploader.dll file. An extended length string can be passed into scripts within the management website on port 80 (the 'uploadfile' multipart form data 'filename' parameter in Default.asp) and ultimately to MPAUploader.dll. As a static stack allocation is used to store the buffer and the string length is not handled properly, a remote attacker may overwrite the stack and ultimately execute remote code.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03128469

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-12-22 - Coordinated public release of advisory

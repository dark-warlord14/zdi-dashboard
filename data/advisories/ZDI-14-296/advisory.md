# ZDI-14-296: Novell Groupwise Administration Server FileUploadServlet poLibMaintenanceFileSave Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-296
- **ZDI-CAN:** ZDI-CAN-2287
- **Date:** 2014-08-26
- **CVE:** CVE-2014-0600
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-296/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of Novell Groupwise. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of the poLibMaintenanceFileSave parameter within the FileUploadServlet. By abusing this flaw an attacker can disclose and destroy arbitrary files on the server and possibly leverage this information to achieve remote code execution in a subsequent attack.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7015566

## Disclosure Timeline

- 2014-04-18 - Vulnerability reported to vendor
- 2014-08-26 - Coordinated public release of advisory

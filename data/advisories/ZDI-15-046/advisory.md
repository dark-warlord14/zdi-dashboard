# ZDI-15-046: Lexmark Markvision Enterprise LibraryFileUploadServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-046
- **ZDI-CAN:** ZDI-CAN-2648
- **Date:** 2015-02-13
- **CVE:** CVE-2014-9375
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Lexmark
- **Affected Products:** MarkVision Enterprise
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Lexmark MarkVision Enterprise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the LibraryFileUploadServlet servlet. By supplying a crafted ZIP archive which includes directory traversal in the archive filenames, an attacker is able to upload files to any location on the system. An attacker could leverage this to execute arbitrary code as SYSTEM.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: http://support.lexmark.com/index?page=content&id=TE677&locale=EN&userlocale=EN_US

## Disclosure Timeline

- 2014-12-04 - Vulnerability reported to vendor
- 2015-02-13 - Coordinated public release of advisory

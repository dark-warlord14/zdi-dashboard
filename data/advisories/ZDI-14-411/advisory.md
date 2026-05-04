# ZDI-14-411: Lexmark MarkVision Enterprise ReportDownloadServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-411
- **ZDI-CAN:** ZDI-CAN-2438
- **Date:** 2014-12-09
- **CVE:** CVE-2014-8742
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Lexmark
- **Affected Products:** MarkVision Enterprise
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-411/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Lexmark MarkVision Enterprise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ReportDownloadServlet class. The class contains a method that does not properly sanitize input allowing for directory traversal. An attacker can leverage this vulnerability to read files under the context of SYSTEM.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: http://support.lexmark.com/index?page=content&id=TE667&locale=EN&userlocale=EN_US

## Disclosure Timeline

- 2014-11-03 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory

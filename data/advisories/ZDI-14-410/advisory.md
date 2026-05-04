# ZDI-14-410: Lexmark MarkVision Enterprise GfdFileUploadServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-410
- **ZDI-CAN:** ZDI-CAN-2437
- **Date:** 2014-12-09
- **CVE:** CVE-2014-8741
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Lexmark
- **Affected Products:** MarkVision Enterprise
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-410/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Lexmark MarkVision Enterprise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GfdFileUploadServlet class. The class contains a method that does not properly sanitize input allowing for directory traversal. An attacker can leverage this vulnerability to write files under the context of SYSTEM and achieve remote code execution.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: http://support.lexmark.com/index?page=content&id=TE666&locale=EN&userlocale=EN_US

## Disclosure Timeline

- 2014-11-03 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory

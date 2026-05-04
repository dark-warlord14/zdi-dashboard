# ZDI-10-297: Novell iPrint Client Netscape/ActiveX Location Header Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-297
- **ZDI-CAN:** ZDI-CAN-978
- **Date:** 2010-12-26
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-297/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. Authentication is not required to exploit this vulnerability. The flaw exists within the nipplib.dll component which is used by both the Mozilla and IE browser plugins for iPrint Client. When handling an HTTP 301 response from a user provided printer-url the process attempts to copy the returned value within the Location HTTP header without ensuring that the destination buffer is adequately sized. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix for this security vulnerability is included in the released "iPrint Client for Windows XP/Vista/Win 7 5.56" patch, available at http://download.novell.com/Download?buildid=JV7fd0tFHHM~ .

## Disclosure Timeline

- 2010-11-30 - Vulnerability reported to vendor
- 2010-12-26 - Coordinated public release of advisory

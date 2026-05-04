# ZDI-10-300: Novell iPrint Client Netscape/ActiveX Plugin HTTP_CONNECTION Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-300
- **ZDI-CAN:** ZDI-CAN-979
- **Date:** 2010-12-26
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-300/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. Authentication is not required to exploit this vulnerability. The flaw exists within the nipplib.dll component used by the the Mozilla and Internet Explorer browser plugins for iPrint client. When parsing an HTTP response the Connection response length is in sufficiently validated before being copied into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix for this security vulnerability is included in the released "iPrint Client for Windows XP/Vista/Win 7 5.56" patch, available at http://download.novell.com/Download?buildid=JV7fd0tFHHM~ .

## Disclosure Timeline

- 2010-11-29 - Vulnerability reported to vendor
- 2010-12-26 - Coordinated public release of advisory

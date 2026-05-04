# ZDI-10-295: Novell iPrint Client Netscape/ActiveX printer-state-reasons Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-295
- **ZDI-CAN:** ZDI-CAN-985
- **Date:** 2010-12-26
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-295/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the both the Netscape (Firefox) and ActiveX (Internet Explorer) plugin components npnipp.dll and ienipp.ocx which are installed by default with the iPrint client. When handling the printer-state-reasons operation provided via the embed tag the module makes a request to the specified printer-url and performs insufficient validation of the size of the printer-state-reasons status response. The process then copies this user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix for this security vulnerability is included in the released "iPrint Client for Windows XP/Vista/Win 7 5.56" patch, available at http://download.novell.com/Download?buildid=JV7fd0tFHHM~ .

## Disclosure Timeline

- 2010-12-06 - Vulnerability reported to vendor
- 2010-12-26 - Coordinated public release of advisory

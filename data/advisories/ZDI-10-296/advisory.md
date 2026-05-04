# ZDI-10-296: Novell iPrint Client Netscape/ActiveX IPP Parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-296
- **ZDI-CAN:** ZDI-CAN-983
- **Date:** 2010-12-26
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-296/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the nipplib.dll component which is used by both the Mozilla and IE browser plugins for iPrint Client. When handling an IPP response from a user provided printer-url the process does not properly validate the size of the destination buffer and copies user supplied data of an arbitrary length into a fixed length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

The fix for this security vulnerability is included in the released "iPrint Client for Windows XP/Vista/Win 7 5.56" patch, available at http://download.novell.com/Download?buildid=JV7fd0tFHHM~ .

## Disclosure Timeline

- 2010-11-30 - Vulnerability reported to vendor
- 2010-12-26 - Coordinated public release of advisory

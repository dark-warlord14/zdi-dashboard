# ZDI-10-153: Apple Webkit SVG Floating Text Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-153
- **ZDI-CAN:** ZDI-CAN-785
- **Date:** 2010-08-11
- **CVE:** CVE-2010-1787
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-153/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's process for handling floating elements within an SVG document. During layout of the element, the application will mismanage references to the floating element. Later the application will attempt to destroy this reference triggering corruption. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Fixed in Safari 5.0.1: http://support.apple.com/kb/HT4276

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-08-11 - Coordinated public release of advisory

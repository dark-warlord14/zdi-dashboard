# ZDI-10-146: Apple Webkit Anchor Tag Mouse Click Event Dispatch Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-146
- **ZDI-CAN:** ZDI-CAN-783
- **Date:** 2010-08-09
- **CVE:** CVE-2010-0048
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-146/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's support for mouse events on a particular element. If a mouse event is dispatched to an element when one of it's attributes is undefined, the library will dereference a memory pointer pointing to arbitrary data. Usage of this element can then lead to code execution under the context of the application.

## Additional Details

http://support.apple.com/kb/HT4225 http://support.apple.com/kb/HT4070

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-08-09 - Coordinated public release of advisory

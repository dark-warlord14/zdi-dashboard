# ZDI-10-154: Apple Webkit Button First-Letter Style Rendering Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-154
- **ZDI-CAN:** ZDI-CAN-791
- **Date:** 2010-08-11
- **CVE:** CVE-2010-1392
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-154/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. Authentication is not required to exploit this vulnerability. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Webkit's support of the 'first-letter' css style. If a particular container has the first-letter style applied to it, the library will create a dual reference of text associated with the style for rendering. Later upon repainting or style recalculation, the application will access the freed memory which can lead to code execution under the context of the application.

## Additional Details

this issue was fixed in Safari 5.0 http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-08-11 - Coordinated public release of advisory

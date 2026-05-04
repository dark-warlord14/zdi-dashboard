# ZDI-10-029: Apple WebKit innerHTML element Substitution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-029
- **ZDI-CAN:** ZDI-CAN-579
- **Date:** 2010-03-15
- **CVE:** CVE-2010-0047
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Google, Apple, Apple
- **Affected Products:** Chrome, Safari, WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the WebCore's HTMLObjectElement::renderFallBackContent() method. By rewriting an HTML element via the document's innerHTML() method a memory corruption occurs resulting from a call-after-free. This can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4070

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-03-15 - Coordinated public release of advisory

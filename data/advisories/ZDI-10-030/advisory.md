# ZDI-10-030: Apple WebKit CSS run-in Attribute Rendering Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-030
- **ZDI-CAN:** ZDI-CAN-578
- **Date:** 2010-03-16
- **CVE:** CVE-2010-0053
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Google, Apple, Apple
- **Affected Products:** Chrome, Safari, WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari and other WebKit based browsers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of the run-in value for display CSS styles. A specially crafted web page can cause a use after free() condition in WebKit's WebCore::RenderBlock() method. This can be further leveraged by attackers to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4070

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-03-16 - Coordinated public release of advisory

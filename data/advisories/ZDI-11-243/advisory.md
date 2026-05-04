# ZDI-11-243: WebKit ContentEditable Inline Style Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-243
- **ZDI-CAN:** ZDI-CAN-1108
- **Date:** 2011-07-27
- **CVE:** CVE-2011-0232
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** J23 -- http://twitter.com/HansJ23
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-243/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit as utilized by either Apple Safari, or Google's Chrome browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the library handles implicitly defined styles. When processing a specific case for a style, the application will dispatch an event. During this dispatch, code can be executed that can be used to manipulate the DOM tree causing a type-switch. This type-switch can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT4808

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-07-27 - Coordinated public release of advisory
- 2020-07-30 - Advisory Updated

# ZDI-12-147: WebKit ContentEditable swapInNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-147
- **ZDI-CAN:** ZDI-CAN-1416
- **Date:** 2012-08-22
- **CVE:** CVE-2011-3897
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** pa_kt / twitter.com/pa_kt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-147/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the WebKit library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the library attempts to replace a particular element due to an HTML5 ContentEditable command. Due to the library not accommodating for DOM mutation events that can be made to occur, an aggressor can modify the tree out from underneath the library, leading to a type change. This can be used to trigger a use-after-free condition at which point can lead to code execution under the context of the application.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: https://bugs.webkit.org/show_bug.cgi?id=71145

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory

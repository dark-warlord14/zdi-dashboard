# ZDI-12-191: Webkit HTMLMedia Element beforeLoad Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-191
- **ZDI-CAN:** ZDI-CAN-1528
- **Date:** 2012-12-21
- **CVE:** CVE-2011-3071
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** pa_kt / twitter.com/pa_kt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's implementation of a HTMLMedia element. After a source element is created, an attacker can catch the beforeLoad event before the element is used, and delete the element. The pointer to the source element will then be referenced causing a use-after-free condition, which can lead to code execution under the context of the application.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory

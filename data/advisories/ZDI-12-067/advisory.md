# ZDI-12-067: WebKit.org Webkit Array.Splice Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-067
- **ZDI-CAN:** ZDI-CAN-1484
- **Date:** 2012-04-18
- **CVE:** CVE-2012-0592
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the JavaScriptCore component as used by WebKit. This module is responsible for the in browser implementation of JavaScript. When handling the array.splice method the browser improperly calculates the length, and thus allocation size for the newly modified array. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://prod.lists.apple.com/archives/security-announce/2012/Mar/msg00003.html

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-04-18 - Coordinated public release of advisory

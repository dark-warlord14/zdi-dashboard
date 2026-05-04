# ZDI-12-054: Webkit fontface Invalid Font Family Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-054
- **ZDI-CAN:** ZDI-CAN-1283
- **Date:** 2012-03-26
- **CVE:** CVE-2011-2825
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** wushi of team509 miaubiz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing and utilization of font objects. When the code parses the @font-face CSS element it does not validate that the font-family is legitimate. Later, if the same font-family is applied within CSS the code will access an invalid element of its internal font object. This can be leveraged by a remote attacker to execute code under the context of the user running the browser.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5190

## Disclosure Timeline

- 2011-07-06 - Vulnerability reported to vendor
- 2012-03-26 - Coordinated public release of advisory

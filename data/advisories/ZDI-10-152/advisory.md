# ZDI-10-152: Apple WebKit RTL LineBox Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-152
- **ZDI-CAN:** ZDI-CAN-703
- **Date:** 2010-08-11
- **CVE:** CVE-2010-0049
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-152/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to the method by which the Webkit library renders right-to-left text. If a linebox has a width greater than it's container, Webkit frees an object that upon page destruction is freed again. An attacker can exploit this to code execute remote code under the context of the application.

## Additional Details

this issue was fixed in Safari 4.0.5, and iOS 4 for iPhone and iPod touch iOS 3.2 iOS 4: http://support.apple.com/kb/HT4225 Safari 4.0.5: http://support.apple.com/kb/HT4070

## Disclosure Timeline

- 2010-02-18 - Vulnerability reported to vendor
- 2010-08-11 - Coordinated public release of advisory

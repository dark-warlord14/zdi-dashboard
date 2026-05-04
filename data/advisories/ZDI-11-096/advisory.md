# ZDI-11-096: Apple Safari WebKit Range Object Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-096
- **ZDI-CAN:** ZDI-CAN-970
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0115
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** J23 -- http://twitter.com/HansJ23
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how WebKit processes a range object as defined with the DOM level 2 specification. When processing the contents of a range, WebKit will fail to accommodate for manipulation of the DOM due to an event listener. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-11-05 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory

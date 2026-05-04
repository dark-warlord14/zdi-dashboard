# ZDI-10-257: Apple Webkit WholeText Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-257
- **ZDI-CAN:** ZDI-CAN-874
- **Date:** 2010-11-23
- **CVE:** CVE-2010-3812
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** J23 (http://twitter.com/HansJ23)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-257/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the wholeText method of the Text element. When calculating the total size of all the text containing it, the application will wrap a 32-bit integer. The application will use this in an allocation and then later use a different value for populating the buffer. This can lead to code execution under the context of the application.

## Additional Details

iOS 4.2: http://support.apple.com/kb/HT4456

## Disclosure Timeline

- 2010-08-12 - Vulnerability reported to vendor
- 2010-11-23 - Coordinated public release of advisory

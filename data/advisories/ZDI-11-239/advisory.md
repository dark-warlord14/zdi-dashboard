# ZDI-11-239: Apple Safari Webkit FrameOwner Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-239
- **ZDI-CAN:** ZDI-CAN-1047
- **Date:** 2011-07-27
- **CVE:** CVE-2011-0233
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-239/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's implementation of a FrameOwner element. When building this tree, the application will create a duplicate reference of an element. By freeing the referenced element, a use-after-free condition can be made to occur which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4808

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-07-27 - Coordinated public release of advisory

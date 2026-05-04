# ZDI-10-170: Apple Safari Webkit Runin Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-170
- **ZDI-CAN:** ZDI-CAN-806
- **Date:** 2010-09-13
- **CVE:** CVE-2010-1806
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-170/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's support of an element containing the run-in property. When a block box is appended as the sibling of a run-in box, the run-in box will be promoted to the first inline box. This implies that the first inline box will be destroyed. Later when the application attempts to destroy this element, it will access memory that has been freed. If an attacker can substitute an alternate type in the element's place, the attacker will have code execution under the context of the application.

## Additional Details

http://support.apple.com/kb/HT4333 http://support.apple.com/kb/HT4456

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory

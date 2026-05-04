# ZDI-10-092: Apple Webkit Option Element ContentEditable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-092
- **ZDI-CAN:** ZDI-CAN-688
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1396
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-092/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apples Webkit. User interaction is required in that the user must coerced into visiting a website or opening a malicious document. The specific flaw exists within how the library removes a particular container element containing another element holding the contentEditable attribute. Upon removal of the container during a particular event, the library will traverse the tree and access the contentEditable element that was freed. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-05-10 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory

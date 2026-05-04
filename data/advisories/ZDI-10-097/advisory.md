# ZDI-10-097: Apple Webkit ContentEditable moveParagraphs Uninitialized Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-097
- **ZDI-CAN:** ZDI-CAN-686
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1398
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-097/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required in that a user must be coerced into visiting a malicious website. The specific flaw exists within the way Webkit inserts an element into an editable container. Immediately before the actual insertion the library will manipulate the contents of the field in order to insert the new node. Upon traversal of the tree by the library, the application will attempt to access an uninitialized element that was created prior to the insertion. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-02-18 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory

# ZDI-10-048: Mozilla Firefox nsTreeContentView Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-048
- **ZDI-CAN:** ZDI-CAN-633
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0176
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.5.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required in that the victim must visit a malicious website or be coerced into opening a malicious document. The specific flaw exists within the way that Mozilla's Firefox parses .XUL files. While appending a particular tag to a treechildren container, the application will create more than one reference to a particular element without increasing its reference count. Upon removal of one of the elements, the refcount will be decreased causing the application to free the memory associated with the object. Due to the rogue reference occurring, the next time the application attempts to reference that container, the application will access memory that has been freed which can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-18.html

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory

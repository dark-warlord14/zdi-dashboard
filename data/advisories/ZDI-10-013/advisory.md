# ZDI-10-013: Microsoft Internet Explorer Table Layout Reuse Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-013
- **ZDI-CAN:** ZDI-CAN-514
- **Date:** 2010-01-21
- **CVE:** CVE-2010-0245
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas of eshu.co.uk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when specific elements are used within a table container. If one of these elements is removed the application will unlink the element from the layout tree incorrectly. When this tree is later traversed, the application will reuse the object that has been freed which can lead to code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-002.mspx

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory

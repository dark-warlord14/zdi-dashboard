# ZDI-09-088: Microsoft Internet Explorer IFrame Attributes Circular Reference Dangling Pointer Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-088
- **ZDI-CAN:** ZDI-CAN-547
- **Date:** 2009-12-08
- **CVE:** CVE-2009-3674
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. The specific flaw exists during deallocation of a circular dereference for a CAttrArray object. If the CAttrArray object has been freed prior to the tearing down of the webpage, the application will access the freed memory during the deallocation of the circular dereference. This can lead to code execution under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-072.mspx

## Disclosure Timeline

- 2009-08-10 - Vulnerability reported to vendor
- 2009-12-08 - Coordinated public release of advisory

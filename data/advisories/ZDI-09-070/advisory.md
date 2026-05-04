# ZDI-09-070: Microsoft Internet Explorer Event Object Type Double-Free Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-070
- **ZDI-CAN:** ZDI-CAN-489
- **Date:** 2009-10-13
- **CVE:** CVE-2009-2530
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Internet Explorer 6, Internet Explorer 7, Internet Explorer 8
- **Credit:** Anonymous Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the copy constructor for a specific DOM object. When duplicated, more than one reference can be made of anything assigned to it's properties. When the variable/object goes out of scope, these properties will be deallocated twice. This results in a heap corruption which can lead to code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-054.mspx

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-10-13 - Coordinated public release of advisory

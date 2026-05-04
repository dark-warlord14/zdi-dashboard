# ZDI-09-011: Microsoft Internet Explorer CFunctionPointer Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-011
- **ZDI-CAN:** ZDI-CAN-391
- **Date:** 2009-02-10
- **CVE:** CVE-2009-0075
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of document objects. When an object is appended and deleted in a specific order memory corruption occurs. Successful exploitation leads to remote compromise of the affected system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-002.mspx

## Disclosure Timeline

- 2008-09-23 - Vulnerability reported to vendor
- 2009-02-10 - Coordinated public release of advisory

# ZDI-08-051: Microsoft Internet Explorer Table Layout Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-051
- **ZDI-CAN:** ZDI-CAN-308
- **Date:** 2008-08-12
- **CVE:** CVE-2008-2258
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of document objects. When an object is appended in a specific order and particular functions are performed on these objects memory corruption occurs. Successful exploitation leads to remote compromise of the affected system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-045.mspx

## Disclosure Timeline

- 2008-04-16 - Vulnerability reported to vendor
- 2008-08-12 - Coordinated public release of advisory

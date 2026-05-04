# ZDI-08-087: Microsoft Internet Explorer Webdav Request Parsing Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-087
- **ZDI-CAN:** ZDI-CAN-331
- **Date:** 2008-12-09
- **CVE:** CVE-2008-4259
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Brett Moore, Insomnia Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-087/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer 7 on the Microsoft Vista operating system. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during a WebDAV fetch of a document from a path containing a large number of characters. Mishandling of cached content results in a heap corruption which can be leveraged to execute arbitrary code under the context of the current instance of Internet Explorer.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-073.mspx

## Disclosure Timeline

- 2008-05-19 - Vulnerability reported to vendor
- 2008-12-09 - Coordinated public release of advisory

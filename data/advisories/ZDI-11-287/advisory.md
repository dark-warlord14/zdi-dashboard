# ZDI-11-287: Internet Explorer Select Element Cache Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-287
- **ZDI-CAN:** ZDI-CAN-1267
- **Date:** 2011-10-15
- **CVE:** CVE-2011-1996
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ivan Fratric http://ifsec.blogspot.com/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the caching implementation of a Select element. When modifying this cache, there are certain methods that do not update the cache correctly. Due to these inconsistencies, one can desynchronize the cache with elements that have been freed. While using these freed elements, the application's perception of type-safety becomes skewed and usage of the object can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms11-081

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2011-10-15 - Coordinated public release of advisory

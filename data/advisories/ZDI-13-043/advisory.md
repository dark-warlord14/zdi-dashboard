# ZDI-13-043: Microsoft Internet Explorer saveHistory Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-043
- **ZDI-CAN:** ZDI-CAN-1649
- **Date:** 2013-03-22
- **CVE:** CVE-2013-0088
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific issue is due to the way Internet Explorer handles elements associated to the saveHistory behavior and an onload event handler. The process can be made to re-use a freed object. This can lead to a use-after-free scenario which can be leveraged to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-021

## Disclosure Timeline

- 2012-10-24 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory

# ZDI-12-065: Microsoft Internet Explorer selectAll Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-065
- **ZDI-CAN:** ZDI-CAN-1471
- **Date:** 2012-04-18
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific issue is due to the way Internet Explorer handles multiple invocations of the selectAll function. When certain objects are created, the process can be made to descend into a function that will delete an object and create a new one, without replacing references that the parent caller will later utilize. This can lead to a use after free scenario which can be leveraged to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-023

## Disclosure Timeline

- 2012-01-12 - Vulnerability reported to vendor
- 2012-04-18 - Coordinated public release of advisory

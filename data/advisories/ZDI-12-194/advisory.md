# ZDI-12-194: Microsoft Internet Explorer OnBeforeDeactivate Event Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-194
- **ZDI-CAN:** ZDI-CAN-1523
- **Date:** 2012-12-21
- **CVE:** CVE-2012-1878
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-194/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles the onbeforedeactivate callback function for certain elements. During the execution of the onbeforedeactivate callback function it is possible to alter the DOM tree of the page which can lead to a use-after-free vulnerability when the function returns. This can result in remote code execution under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms12-037

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory

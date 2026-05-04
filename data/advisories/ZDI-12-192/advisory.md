# ZDI-12-192: Microsoft Internet Explorer insertRow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-192
- **ZDI-CAN:** ZDI-CAN-1525
- **Date:** 2012-12-21
- **CVE:** CVE-2012-1880
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles consecutive calls to insertRow. When the number of rows reaches a certain threshold the program fails to correctly relocate certain key objects. This can lead to a use-after-free vulnerability which can result in remote code execution under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms12-037

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory

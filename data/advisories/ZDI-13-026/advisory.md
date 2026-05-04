# ZDI-13-026: Microsoft Internet Explorer CDispNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-026
- **ZDI-CAN:** ZDI-CAN-1683
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0023
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Arthur Gerkis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific issue is due to the way Internet Explorer handles SVG objects. A use-after-free condition can be created when an SVG references a self-referent SVG. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS13-009

## Disclosure Timeline

- 2012-11-20 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory

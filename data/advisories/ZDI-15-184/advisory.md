# ZDI-15-184: Microsoft Internet Explorer CElement::DelMarkupPtr Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-184
- **ZDI-CAN:** ZDI-CAN-2780
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1706
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zheng Huang of Baidu Scloud XTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-184/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer stores pointers to CMarkup objects. By manipulating a document's elements an attacker can force a pointer to a CSecurityContext object in memory to be interpreted as a pointer to a CMarkup object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-043

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory

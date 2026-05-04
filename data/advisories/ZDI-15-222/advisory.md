# ZDI-15-222: Microsoft Internet Explorer Tree::TableGridBlock Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-222
- **ZDI-CAN:** ZDI-CAN-2855
- **Date:** 2015-05-14
- **CVE:** CVE-2015-1709
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zheng Huang of Baidu Scloud XTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-222/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Tree::TableGridBlock objects. By manipulating a document's elements, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-043

## Disclosure Timeline

- 2015-04-09 - Vulnerability reported to vendor
- 2015-05-14 - Coordinated public release of advisory

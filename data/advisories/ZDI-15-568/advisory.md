# ZDI-15-568: Microsoft Internet Explorer TreeWalker Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-568
- **ZDI-CAN:** ZDI-CAN-3024
- **Date:** 2015-11-12
- **CVE:** CVE-2015-1767
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zheng Huang of Baidu Scloud XTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-568/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to TreeWalker objects. By manipulating a document's elements an attacker can force a CTreeNode object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-065

## Disclosure Timeline

- 2015-07-02 - Vulnerability reported to vendor
- 2015-11-12 - Coordinated public release of advisory

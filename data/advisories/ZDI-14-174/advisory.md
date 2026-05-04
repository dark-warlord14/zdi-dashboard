# ZDI-14-174: Microsoft Internet Explorer CGeneratedTreeNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-174
- **ZDI-CAN:** ZDI-CAN-2025
- **Date:** 2014-06-11
- **CVE:** CVE-2014-1774
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AMol NAik
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-174/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CGeneratedTreeNode objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms14-035

## Disclosure Timeline

- 2013-11-07 - Vulnerability reported to vendor
- 2014-06-11 - Coordinated public release of advisory

# ZDI-15-102: Microsoft Internet Explorer SVG marker Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-102
- **ZDI-CAN:** ZDI-CAN-2736
- **Date:** 2015-03-12
- **CVE:** CVE-2015-0043
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability lies in the handling of SVG marker elements. By manipulating a document's elements an attacker can force a CGeneratedTreeNode object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2015-02-05 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory

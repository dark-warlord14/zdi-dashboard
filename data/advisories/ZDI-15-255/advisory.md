# ZDI-15-255: Microsoft Internet Explorer CListItemMarker Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-255
- **ZDI-CAN:** ZDI-CAN-2767
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1622
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AMol NAik
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes CSS-defined list item markers. By manipulating a document's elements an attacker can force a CGeneratedTreeNode object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-018

## Disclosure Timeline

- 2015-02-24 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory

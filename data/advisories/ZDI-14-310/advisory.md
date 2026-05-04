# ZDI-14-310: Microsoft Internet Explorer CGeneratedTreeNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-310
- **ZDI-CAN:** ZDI-CAN-2364
- **Date:** 2014-09-16
- **CVE:** CVE-2014-4098
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-310/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles CSS generated content. By creating an HTML document that is malformed in a particular way and then adding CSS generated content, an attacker can force a CGeneratedTreeNode object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-052

## Disclosure Timeline

- 2014-06-03 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory

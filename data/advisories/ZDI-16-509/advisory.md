# ZDI-16-509: Microsoft Edge TextNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-509
- **ZDI-CAN:** ZDI-CAN-3782
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3294
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Shi Ji (@Puzzor) of VARAS@IIE
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-509/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw relates to how Edge handles text nodes within HTML documents. By manipulating a document's elements an attacker can force a Tree::TextNode object in memory to be reused as a Tree::ANode object after it has already been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-105

## Disclosure Timeline

- 2016-05-23 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory

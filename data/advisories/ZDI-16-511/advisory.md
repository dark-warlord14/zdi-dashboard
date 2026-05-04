# ZDI-16-511: Microsoft Edge CTreePos Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-511
- **ZDI-CAN:** ZDI-CAN-3792
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3295
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Garage4Hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-511/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw relates to how Edge handles text nodes within HTML documents. By manipulating a document's elements an attacker can cause Microsoft Edge to use a pointer to a CTreePos as if it were a pointer to a Tree::ANode. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-105

## Disclosure Timeline

- 2016-05-26 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory

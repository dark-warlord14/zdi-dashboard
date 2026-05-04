# ZDI-16-165: Microsoft Edge Text Node Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-165
- **ZDI-CAN:** ZDI-CAN-3368
- **Date:** 2016-02-10
- **CVE:** CVE-2016-0060
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** 003
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-165/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Microsoft Edge processes text nodes within document fragments. By manipulating a document's elements an attacker can cause Microsoft Edge to use a flag value as if it were a pointer to a Tree::ANode object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-009

## Disclosure Timeline

- 2015-11-02 - Vulnerability reported to vendor
- 2016-02-10 - Coordinated public release of advisory

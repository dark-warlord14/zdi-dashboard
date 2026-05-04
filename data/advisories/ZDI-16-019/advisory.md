# ZDI-16-019: Microsoft Edge TextData Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-019
- **ZDI-CAN:** ZDI-CAN-3329
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0003
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** 003
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-019/
## Vulnerability Details

This vulnerability allows remote attackers to disclose the contents of memory on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of text nodes within HTML documents. By manipulating a document's elements an attacker can disclose the contents of memory. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-002

## Disclosure Timeline

- 2015-10-08 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory

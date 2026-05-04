# ZDI-16-411: Microsoft Edge InjectHtmlStream Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-411
- **ZDI-CAN:** ZDI-CAN-3691
- **Date:** 2016-07-12
- **CVE:** CVE-2016-3246
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** cc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-411/
## Vulnerability Details

This vulnerability allows remote attackers to corrupt memory on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within InjectHtmlStream. By manipulating a document's elements an attacker can reveal the contents of memory and also cause memory corruption. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-085

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory

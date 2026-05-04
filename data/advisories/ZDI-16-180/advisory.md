# ZDI-16-180: Microsoft Internet Explorer CDataset RemoveItem Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-180
- **ZDI-CAN:** ZDI-CAN-3455
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0106
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** sky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-180/
## Vulnerability Details

This vulnerability allows remote attackers to disclose the contents of memory on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles custom data attributes attached to HTML elements. By manipulating a document's elements an attacker can force a string in memory to be reused after it has been freed, leading to a disclosure of memory contents. An attacker can use this information in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-023

## Disclosure Timeline

- 2015-12-07 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory

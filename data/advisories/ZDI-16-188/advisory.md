# ZDI-16-188: Microsoft Internet Explorer setAttribute Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-188
- **ZDI-CAN:** ZDI-CAN-3492
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0112
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** sky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-188/
## Vulnerability Details

This vulnerability allows remote attackers to disclose memory contents on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles changes to attributes of DOM elements. By manipulating a document's elements an attacker can cause a string allocation in memory to be reused after it has been freed. An attacker can leverage this vulnerability to disclose memory contents.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-023

## Disclosure Timeline

- 2016-01-05 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory

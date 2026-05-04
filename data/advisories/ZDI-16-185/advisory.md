# ZDI-16-185: Microsoft Internet Explorer CAttrArray Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-185
- **ZDI-CAN:** ZDI-CAN-3488
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0112
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0011
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles attributes of DOM elements. By manipulating a document's elements an attacker can cause Internet Explorer to process a string as if it were a CAttrArray object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-023

## Disclosure Timeline

- 2016-01-05 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory

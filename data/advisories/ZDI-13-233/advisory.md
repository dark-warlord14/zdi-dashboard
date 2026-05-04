# ZDI-13-233: Microsoft Internet Explorer HtmlLayout::SmartObject Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-233
- **ZDI-CAN:** ZDI-CAN-1941
- **Date:** 2013-10-08
- **CVE:** CVE-2013-3873
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Jose A. Vazquez of Yenteasy - Security Research -
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-233/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HtmlLayout::SmartObject objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-080

## Disclosure Timeline

- 2013-07-23 - Vulnerability reported to vendor
- 2013-10-08 - Coordinated public release of advisory

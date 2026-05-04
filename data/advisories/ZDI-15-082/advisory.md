# ZDI-15-082: Microsoft Internet Explorer CGeneratedContent::UnWrapContent Out-Of-Bound Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-082
- **ZDI-CAN:** ZDI-CAN-2655
- **Date:** 2015-03-10
- **CVE:** CVE-2015-1622
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-082/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within style processing of HTML elements. By manipulating styles of an element, an attacker can force Internet Explorer to modify memory past the end of the element. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-018

## Disclosure Timeline

- 2014-12-04 - Vulnerability reported to vendor
- 2015-03-10 - Coordinated public release of advisory

# ZDI-14-356: Microsoft Internet Explorer CElement::DelMarkupPtr Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-356
- **ZDI-CAN:** ZDI-CAN-2388
- **Date:** 2014-10-14
- **CVE:** CVE-2014-4145
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-356/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The issue lies in CElement::DelMarkupPtr which expects a CMarkup object at a certain offset. By calling CElement::DelMarkupPtr more than once an attacker can force type confusion that leads to an out-of-bounds read. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS14-051

## Disclosure Timeline

- 2014-06-30 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory

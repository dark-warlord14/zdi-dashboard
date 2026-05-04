# ZDI-15-645: Microsoft Internet Explorer TextBlock Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-645
- **ZDI-CAN:** ZDI-CAN-3440
- **Date:** 2015-12-17
- **CVE:** CVE-2015-6159
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Jason Kratzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-645/
## Vulnerability Details

This vulnerability allows remote attackers to leak sensitive information on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the DOM after changing the text direction. By manipulating a document's elements an attacker can force an out-of-bounds read. An attacker can leverage this vulnerability to leak sensitive information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-124.aspx

## Disclosure Timeline

- 2015-12-03 - Vulnerability reported to vendor
- 2015-12-17 - Coordinated public release of advisory

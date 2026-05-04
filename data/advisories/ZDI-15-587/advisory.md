# ZDI-15-587: Microsoft Internet Explorer CAttrArray Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-587
- **ZDI-CAN:** ZDI-CAN-3319
- **Date:** 2015-12-08
- **CVE:** CVE-2015-6142
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-587/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes style attributes. By manipulating a document's elements an attacker can force an array allocated by a CStyleAttrArray object to be processed as if it were a CAttrArray object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-124.aspx

## Disclosure Timeline

- 2015-09-17 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory

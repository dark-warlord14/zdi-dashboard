# ZDI-10-197: Microsoft Internet Explorer Stylesheet PrivateFind Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-197
- **ZDI-CAN:** ZDI-CAN-826
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3328
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the function CAttrArray::PrivateFind as defined in mshtml.dll. If a specific property of a stylesheet object is set, the code within mshtml can be forced to free an object which is subsequently accessed later. This can be leveraged by an attacker to execute remote code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-071.mspx

## Disclosure Timeline

- 2010-06-08 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory

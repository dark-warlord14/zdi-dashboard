# ZDI-11-196: Microsoft Internet Explorer HTTP 302 Redirect Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-196
- **ZDI-CAN:** ZDI-CAN-1146
- **Date:** 2011-06-14
- **CVE:** CVE-2011-1262
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Internet Explorer 9, Internet Explorer 8
- **Credit:** Peter Winter-Smith
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-196/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles HTTP 302 redirects to CDL protocols. When Internet Explorer tries to determine who is responsible for handling the protocol redirect it fails to keep a correct reference counter to a Transaction object which results in a use-after-free vulnerability. This can be leveraged into remote code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-050.mspx

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

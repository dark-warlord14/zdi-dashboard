# ZDI-11-247: Microsoft Internet Explorer XSLT SetViewSlave Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-247
- **ZDI-CAN:** ZDI-CAN-1224
- **Date:** 2011-08-09
- **CVE:** CVE-2011-1963
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-247/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the part of the application that is responsible for reloading the markup for a root document object. During reloading of the markup, the application will dispatch a notification whilst retaining a reference to the object in the function's context. This can allow an event callback to tamper with the root document object. Usage of this malformed object can then be used to achieve code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS11-057.mspx

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-08-09 - Coordinated public release of advisory

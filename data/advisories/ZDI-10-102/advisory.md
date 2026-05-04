# ZDI-10-102: Microsoft Internet Explorer Stylesheet Array Removal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-102
- **ZDI-CAN:** ZDI-CAN-763
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1262
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Peter Vreugdenhil (http://twitter.com/WTFuzz)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required in that a target must visit a malicious page. The specific flaw exists within IE's support for the CStyleSheet object. When a style sheet array is created it contains a reference to it's root container. If the stylesheet was created as part of an element not in a markup the root container can be freed when that element is destroyed. When the application attempts to use the stylesheet after this, an invalid pointer is utilized. This can be leveraged by attackers to execute arbitrary code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-035.mspx

## Disclosure Timeline

- 2010-03-26 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory

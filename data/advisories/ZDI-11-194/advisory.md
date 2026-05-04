# ZDI-11-194: Microsoft Internet Explorer layout-grid-char style Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-194
- **ZDI-CAN:** ZDI-CAN-1155
- **Date:** 2011-06-14
- **CVE:** CVE-2011-1260
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Internet Explorer 9, Internet Explorer 8
- **Credit:** Jose A. Vazquez of {http://spa-s3c.blogspot.com}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-194/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles unusual values for the layout-grid-char style property. Specific values may result in the destruction of a tree node that is still in use during the rendering of the HTML page. The resulting use-after-free vulnerability can be leveraged to achieve remote code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-050.mspx

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

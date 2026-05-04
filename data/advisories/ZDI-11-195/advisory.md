# ZDI-11-195: Microsoft Internet Explorer selection.empty Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-195
- **ZDI-CAN:** ZDI-CAN-1137
- **Date:** 2011-06-14
- **CVE:** CVE-2011-1261
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Internet Explorer 9, Internet Explorer 8
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-195/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet explorer handles the javascript statement 'selection.empty' during certain onclick events. By causing a particular sequence of events, an attacker can cause a CDisplayObject to be freed while it is still in use. This results in an operation on previously freed memory that can be utilized to achieve remote code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-050.mspx

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

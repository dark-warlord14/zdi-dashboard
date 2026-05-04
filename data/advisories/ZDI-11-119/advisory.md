# ZDI-11-119: (Pwn2Own) Microsoft Internet Explorer onPropertyChange Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-119
- **ZDI-CAN:** ZDI-CAN-1157
- **Date:** 2011-04-12
- **CVE:** CVE-2011-1345
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles onPropertyChange function calls. When the onPropertyChange event handler is set to an object's attribute collection, it fails to keep an accurate reference counter to the event object. The effect of this can be that the program frees the event object while there are still references to it. This can result in remote code execution under the content of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-018.mspx

## Disclosure Timeline

- 2011-03-09 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory

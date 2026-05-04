# ZDI-11-290: Microsoft Internet Explorer SetExpandedClipRect Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-290
- **ZDI-CAN:** ZDI-CAN-1324
- **Date:** 2011-10-15
- **CVE:** CVE-2011-2001
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within mshtml.dll and is a logic bug in the way it handles the 'extra size index' in certain CDispNode classes within the SetExpandedClipRect function. When the 'extra size index' is zero, the code fails to correctly adjust the class instance pointer before and uses the vftable pointer as a flag field. This corrupts the vftable pointer and can lead to remote code execution under the context of the current user. This issue is closely related to CVE-2009-3672.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms11-081

## Disclosure Timeline

- 2011-07-21 - Vulnerability reported to vendor
- 2011-10-15 - Coordinated public release of advisory

# ZDI-12-190: Microsoft Internet Explorer Title Element Change Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-190
- **ZDI-CAN:** ZDI-CAN-1520
- **Date:** 2012-12-21
- **CVE:** CVE-2012-1877
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 9
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-190/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the 'onpropertychange' user callback function for the document.title. If the function changes the document in the callback function by using, for example, a document.write call, this can result in a use-after-free vulnerability. This can lead to remote code execution under the context of the program.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms12-037

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory

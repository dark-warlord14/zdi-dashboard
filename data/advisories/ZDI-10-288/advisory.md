# ZDI-10-288: Microsoft Internet Explorer Recursive Select Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-288
- **ZDI-CAN:** ZDI-CAN-825
- **Date:** 2010-12-14
- **CVE:** CVE-2010-3345
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's support for the select tag. Upon adding a particular element to the select tag, the application will free the contents of the select element and then use it. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-090.mspx

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-12-14 - Coordinated public release of advisory

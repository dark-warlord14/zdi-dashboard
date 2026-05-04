# ZDI-11-347: Microsoft Office Word Hidden Border Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-347
- **ZDI-CAN:** ZDI-CAN-1085
- **Date:** 2011-12-13
- **CVE:** CVE-2011-1983
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Nikita Tarakanov (CISS Research Team) and Alexey Sintsov (Digital Security Research Group)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-347/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word 2007/2010. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application handles a border containing a specific property. When parsing this property, the application will incorrectly free it. If the application attempts to render the object, a use-after-free condition can be made to occur. This can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS11-089

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-12-13 - Coordinated public release of advisory

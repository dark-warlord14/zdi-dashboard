# ZDI-10-017: Microsoft Office PowerPoint Viewer TextBytesAtom Record Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-017
- **ZDI-CAN:** ZDI-CAN-590
- **Date:** 2010-02-09
- **CVE:** CVE-2010-0033
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint Viewer
- **Credit:** SkD Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office PowerPoint Viewer. User interaction is required to exploit this vulnerability in that the target must open a malicious presentation. The specific flaw exists in the handling of TextBytesAtom records contained in a PPT file. Due to the lack of bounds checking on the size argument an unchecked memcpy() copies user data from the file to the stack, overflowing key exception structures. Exploitation of this vulnerability can lead to remote compromise of the affected system under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS10-004.mspx

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-02-09 - Coordinated public release of advisory

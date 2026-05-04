# ZDI-11-043: (0Day) Microsoft Office Drawing Object Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-043
- **ZDI-CAN:** ZDI-CAN-798
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0977
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Office PowerPoint, Office Excel, Office Word
- **Credit:** Anonymous Aniway (Aniway.Anyway AT gmail DOT com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Excel 2007. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's support for the office drawing file format. When parsing shape data within a particular container, the application will add a reference to an object to a linked list. If an error occurs during parsing, the application will free each element yet fail to remove the reference. Afterward, the application will use this reference. This can lead to code execution under the context of the application.

## Additional Details

Patched April 12, 2011 http://www.microsoft.com/technet/security/Bulletin/MS11-023.mspx

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory

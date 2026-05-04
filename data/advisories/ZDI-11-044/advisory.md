# ZDI-11-044: (0Day) Microsoft PowerPoint 2007 OfficeArt Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-044
- **ZDI-CAN:** ZDI-CAN-827
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0976
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Powerpoint 2007. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists with the way the application will parse external objects within an Office Art container. When parsing this object, the application will append an uninitialized object to a list. When destroying this object during document close (WM_DESTROY), the application will access a method that doesn't exist. This can lead to code execution under the context of the application.

## Additional Details

Patched April 12, 2011 http://www.microsoft.com/technet/security/Bulletin/MS11-022.mspx

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory

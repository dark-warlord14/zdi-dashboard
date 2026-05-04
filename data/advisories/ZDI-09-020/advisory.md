# ZDI-09-020: Microsoft Office PowerPoint Notes Container Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-020
- **ZDI-CAN:** ZDI-CAN-355
- **Date:** 2009-05-12
- **CVE:** CVE-2009-1130
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** ling&wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office's PowerPoint. User interaction is required to exploit this vulnerability in that the target must open up a malicious file. The vulnerability exists within the parsing of certain structures inside a Notes container. During population of a C++ object when reading the Notes container, Powerpoint incorrectly reads more data than was allocated for overwriting a function pointer for the object which is later used in a call from mso.dll. Successful exploitation can lead to remote code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-017.mspx

## Disclosure Timeline

- 2008-06-25 - Vulnerability reported to vendor
- 2009-05-12 - Coordinated public release of advisory

# ZDI-09-045: Microsoft DirectShow Quicktime Atom Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-045
- **ZDI-CAN:** ZDI-CAN-389
- **Date:** 2009-07-14
- **CVE:** CVE-2009-1539
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows 2000, Windows XP, Windows Server 2003
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required in that a target must visit a malicious page or open a malicious video file. The specific flaw exists within the parsing of the length records of certain QuickTime atoms. The application implicitly trusts the length during a transformation which will lead to memory corruption and can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-028.mspx

## Disclosure Timeline

- 2008-09-23 - Vulnerability reported to vendor
- 2009-07-14 - Coordinated public release of advisory

# ZDI-09-019: Microsoft Office PowerPoint OutlineTextRefAtom Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-019
- **ZDI-CAN:** ZDI-CAN-299
- **Date:** 2009-05-12
- **CVE:** CVE-2009-0556
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Marsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office PowerPoint. Exploitation requires that the attacker coerce the target into opening a malicious .PPT file. The specific flaw exists in the parsing of the OutlineTextRefAtom (3998). By specifying an invalid "index" value during parsing memory corruption occurs. Proper exploitation can lead to remote code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-017.mspx

## Disclosure Timeline

- 2008-04-07 - Vulnerability reported to vendor
- 2009-05-12 - Coordinated public release of advisory

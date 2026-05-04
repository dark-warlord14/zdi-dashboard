# ZDI-08-086: Microsoft Office Word Document Table Property Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-086
- **ZDI-CAN:** ZDI-CAN-377
- **Date:** 2008-12-09
- **CVE:** CVE-2008-4837
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** wushi&ling of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-086/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. Exploitation requires that the attacker coerce the target into opening a malicious .DOC file. The specific flaw exists when processing a malformed table property within a Microsoft Word document. User-supplied data is copied into a stack-based buffer using a size that is calculated from the contents of the property. Exploitation can result in arbitrary code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-072.mspx

## Disclosure Timeline

- 2008-08-19 - Vulnerability reported to vendor
- 2008-12-09 - Coordinated public release of advisory

# ZDI-08-084: Microsoft Office RTF Consecutive Drawing Object Parsing Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-084
- **ZDI-CAN:** ZDI-CAN-334
- **Date:** 2008-12-09
- **CVE:** CVE-2008-4027
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Office Word, Outlook
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page, open a malicious e-mail, or open a malicious file. The specific flaw exists when parsing malformed RTF documents. When processing consecutive "\do" Drawing Object tags mso.dll does not properly verify the integrity of the object and frees a memory buffer twice, leading to heap corruption. Successful exploitation can lead to remote compromise of a system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-072.mspx

## Disclosure Timeline

- 2008-05-19 - Vulnerability reported to vendor
- 2008-12-09 - Coordinated public release of advisory

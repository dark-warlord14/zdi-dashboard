# ZDI-08-023: Microsoft Office RTF Parsing Engine Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-023
- **ZDI-CAN:** ZDI-CAN-284
- **Date:** 2008-05-13
- **CVE:** CVE-2008-1091
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Office Word, Office Excel
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page, open a malicious email, or open a malicious file. The specific flaw exists when parsing malformed RTF documents. When processing a combination of RTF tags a heap overflow occurs. Successful exploitation can lead to remote compromise of a system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms08-026.mspx

## Disclosure Timeline

- 2008-01-21 - Vulnerability reported to vendor
- 2008-05-13 - Coordinated public release of advisory

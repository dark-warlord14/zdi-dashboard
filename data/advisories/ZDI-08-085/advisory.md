# ZDI-08-085: Microsoft Office RTF Drawing Object Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-085
- **ZDI-CAN:** ZDI-CAN-351
- **Date:** 2008-12-09
- **CVE:** CVE-2008-4028
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Outlook, Office Word
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-085/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of various Microsoft products including Word and Outlook. User interaction is required to exploit this vulnerability in that the target must visit a malicious page, open a malicious e-mail, or open a malicious file. The specific flaw exists within the parsing of RTF documents containing multiple drawing object tags. First, code within wwlib.dll allocates a buffer for the tag object. Later, a result from a call into mso.dll is copied into the same buffer but with a larger size than was allocated by the callee. Successful exploitation can lead to remote compromise of a system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-072.mspx

## Disclosure Timeline

- 2008-06-25 - Vulnerability reported to vendor
- 2008-12-09 - Coordinated public release of advisory

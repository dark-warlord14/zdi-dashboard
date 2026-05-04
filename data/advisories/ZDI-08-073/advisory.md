# ZDI-08-073: Adobe Acrobat Reader Malformed PDF Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-073
- **ZDI-CAN:** ZDI-CAN-302
- **Date:** 2008-11-04
- **CVE:** CVE-2008-4813
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Javier Vicente Vallejo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat and Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious web address or open a malicious file. The specific flaw exists within the parsing of PDF objects defined in the file. When a specific object becomes malformed, a small memory corruption occurs which can be leveraged by an attacker to execute arbitrary code under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb08-19.html

## Disclosure Timeline

- 2008-04-08 - Vulnerability reported to vendor
- 2008-11-04 - Coordinated public release of advisory

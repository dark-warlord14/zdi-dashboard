# ZDI-08-074: Adobe Acrobat PDF Javascript getCosObj Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-074
- **ZDI-CAN:** ZDI-CAN-329
- **Date:** 2008-11-04
- **CVE:** CVE-2008-4813
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of Adobe Acrobat. User interaction is required in that a user must visit a malicious web site. The specific flaw exists when processing malicious javascript contained in a PDF document. When creating a Collab object and performing a specific sequence of actions on it, memory corruption occurs potentially resulting in remote code execution. If successfully exploited full control of the affected machine running under the credentials of the currently logged in user can be achieved.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb08-19.html

## Disclosure Timeline

- 2008-05-12 - Vulnerability reported to vendor
- 2008-11-04 - Coordinated public release of advisory

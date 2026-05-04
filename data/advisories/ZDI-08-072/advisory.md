# ZDI-08-072: Adobe Acrobat PDF Javascript printf Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-072
- **ZDI-CAN:** ZDI-CAN-283
- **Date:** 2008-11-04
- **CVE:** CVE-2008-2992
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the handling of embedded Javascript code when opening a PDF. Adobe Acrobat has defined it's own set of Javascript functions that can be used in a PDF file. Due to improper parameter checking to one of these functions arbitrary memory can be over-written leading to remote code execution. If successfully exploited remote control of the target system can be gained with the credentials of the logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb08-19.html

## Disclosure Timeline

- 2008-01-21 - Vulnerability reported to vendor
- 2008-11-04 - Coordinated public release of advisory

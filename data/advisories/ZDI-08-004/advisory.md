# ZDI-08-004: Adobe Acrobat Javascript for PDF Integer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-004
- **ZDI-CAN:** ZDI-CAN-262
- **Date:** 2008-02-11
- **CVE:** CVE-2008-0726
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat and Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious web address or open a malicious file. The specific flaw exists in the parsing of embedded JavaScript code within PDF documents. When the function printSepsWithParams() is called with certain malicious parameter values an integer overflow can occur resulting in a memory corruption. This may be subsequently leveraged to execute arbitrary code under the privileges of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/advisories/apsa08-01.html

## Disclosure Timeline

- 2007-11-14 - Vulnerability reported to vendor
- 2008-02-11 - Coordinated public release of advisory

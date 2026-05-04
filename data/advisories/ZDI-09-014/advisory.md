# ZDI-09-014: Adobe Acrobat getIcon() Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-014
- **ZDI-CAN:** ZDI-CAN-362
- **Date:** 2009-03-24
- **CVE:** CVE-2009-0927
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat and Adobe Reader. User interaction is required in that a user must visit a malicious web site or open a malicious file. The specific flaw exists when processing malicious JavaScript contained in a PDF document. When supplying a specially crafted argument to the getIcon() method of a Collab object, proper bounds checking is not performed resulting in a stack overflow. If successfully exploited full control of the affected machine running under the credentials of the currently logged in user can be achieved.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-04.html

## Disclosure Timeline

- 2008-07-03 - Vulnerability reported to vendor
- 2009-03-24 - Coordinated public release of advisory

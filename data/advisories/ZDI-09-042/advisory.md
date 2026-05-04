# ZDI-09-042: Adobe Reader U3D RHAdobeMeta Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-042
- **ZDI-CAN:** ZDI-CAN-433
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1855
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat and Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious web address or open a malicious file. The specific flaw exists when parsing malformed U3D model files contained in a PDF. When a specially crafted extension block of a model is processed, insufficient bounds checking is done before a call to wcsncpy(). Because of this a stack overflow can occur resulting in reliable code execution. Proper exploitation of this vulnerability will result in system compromise under the credentials of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-07.html

## Disclosure Timeline

- 2009-02-24 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory

# ZDI-09-073: Adobe Reader Compact Font Format Malformed Index Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-073
- **ZDI-CAN:** ZDI-CAN-479
- **Date:** 2009-10-13
- **CVE:** CVE-2009-2985
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe, Adobe
- **Affected Products:** Acrobat, Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat and Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application parses a PDF file containing a malformed Compact Font Format stream. While decoding the font embedded in this stream, the application will explicitly trust a 16-bit value used to index into an array of elements. Usage of the object later will cause heap corruption which can be leveraged to achieve code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-15.html

## Disclosure Timeline

- 2009-04-28 - Vulnerability reported to vendor
- 2009-10-13 - Coordinated public release of advisory

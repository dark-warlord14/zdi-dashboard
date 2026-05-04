# ZDI-11-284: Adobe Reader Compound Glyphs Array Indexing Error Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-284
- **ZDI-CAN:** ZDI-CAN-1308
- **Date:** 2011-10-13
- **CVE:** CVE-2011-2441
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-284/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Adobe Reader handles Compound Glyphs. It is possible for an compound glyph to reference another compound glyph. When this happens the Reader fails to correctly count the number of child glyphs. The result is that the code reads a value from outside an array of valid values. This value is used as a counter for a loop that copies memory. This could result in remote code execution under trhe context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-10-13 - Coordinated public release of advisory

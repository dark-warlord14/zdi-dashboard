# ZDI-11-310: Adobe Reader Compound Glyph Index Sign Extension Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-310
- **ZDI-CAN:** ZDI-CAN-1309
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2441
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-310/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Adobe Reader handles compound glyphs. When a glyph has more then 0x7FFF 'numberOfContours' a sign extension occurs resulting in a buffer under-read. Simple glyphs are checked when Adobe Reader parses the font info, but the value for 'numberOfContours' in an compound glyph is the sum of all its child glyphs, and this is not checked. This could result in remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory

# ZDI-10-076: Apple Preview libFontParser SpecialEncoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-076
- **ZDI-CAN:** ZDI-CAN-760
- **Date:** 2010-04-14
- **CVE:** CVE-2010-1120
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Preview
- **Credit:** Charlie Miller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Preview. User interaction is required in that a target must open a malicious file or visit a malicious page. The specific flaw exists within the routine TType1ParsingContext::SpecialEncoding() defined in libFontParser.dylib. While parsing glyphs from a PDF document, a malformed offset greater than 0x400 can result in a heap corruption which can be leveraged by an attacker to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4131

## Disclosure Timeline

- 2010-03-26 - Vulnerability reported to vendor
- 2010-04-14 - Coordinated public release of advisory

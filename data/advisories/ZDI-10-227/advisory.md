# ZDI-10-227: Adobe Shockwave Player Lnam Chunk String Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-227
- **ZDI-CAN:** ZDI-CAN-909
- **Date:** 2010-10-29
- **CVE:** CVE-2010-3655
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** binaryproof Aniway (Aniway.Anyway@gmail.com) Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-227/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the support for parsing Director movies. The .dir format is RIFF-based and is parsed mainly by the dirapi.dll module distributed with Shockwave. While parsing the Lnam chunk within a DIR file, the process attempts to extract a string into a fixed-length buffer located on the stack. The string is prefixed with a one byte size value. If the value is 0xFF the process blindly copies the following string until a NULL byte is found. This can be abused by an attacker to overflow the stack buffer and consequently execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-25.html

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-10-29 - Coordinated public release of advisory

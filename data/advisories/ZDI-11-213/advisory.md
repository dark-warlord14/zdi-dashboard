# ZDI-11-213: Adobe Shockwave rcsL Trusted Offset Chunk Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-213
- **ZDI-CAN:** ZDI-CAN-1072
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2114
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-213/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the rcsL RIFF chunk within Director files. When handling specific structures within this chunk, the process trusts an offset and uses it to calculate a pointer value. By modifying this element an attacker can force the application to corrupt memory at a controlled location. This can be leveraged by an attacker to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

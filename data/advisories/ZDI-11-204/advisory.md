# ZDI-11-204: Adobe Shockwave TextXtra Text Element Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-204
- **ZDI-CAN:** ZDI-CAN-1119
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2112
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-204/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TextXtra.x32 module responsible for parsing text elements within RIFF-based Director files. The code within this module trusts various length and count values present in the file. By crafting certain values an attacker can wrap arithmetic operations and subsequently under-allocate a heap buffer. This can be leveraged to execute remote code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

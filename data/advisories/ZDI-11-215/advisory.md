# ZDI-11-215: Adobe Shockwave DEMX Chunk Multiple Field Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-215
- **ZDI-CAN:** ZDI-CAN-1207
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2112
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-215/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TextXtra.x32 module responsible for parsing text elements within RIFF-based Director files. The code within this module trusts various length and count values present in the file. A boundary error exists when processing the data section of DEMX chunks, which subsequently leads to a stack-based buffer overflow. This can be leveraged to execute remote code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-20 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

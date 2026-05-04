# ZDI-11-080: Adobe Shockwave CSWV Chunk Substructure Offset Value Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-080
- **ZDI-CAN:** ZDI-CAN-990
- **Date:** 2011-02-08
- **CVE:** CVE-2010-4190
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Aniway (Aniway.Anyway@gmail.com) Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing substructures referenced by the CSWV RIFF chunk. An offset is improperly calculated from several elements of a substructure. By crafting a director file in a particular way, an attacker can cause the process to seek out of the bounds of a heap allocation. Due to the way the process continues to manipulate memory, an attacker can force reliable corruption that can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-01.html

## Disclosure Timeline

- 2010-11-29 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory

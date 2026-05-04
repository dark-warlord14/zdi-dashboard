# ZDI-11-220: Adobe Shockwave Director File rcsL Chunk Multiple Opcode Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-220
- **ZDI-CAN:** ZDI-CAN-1074
- **Date:** 2011-06-15
- **CVE:** CVE-2011-0335
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-220/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the RIFF-based Director (.dir) files. When handling an undocumented substructure, the code within dirapi.dll can be forced to incorrectly calculate a destination pointer if it encounters certain 1-byte opcodes within the .dir file. The assumptions made by the code can allow for malicious values to influence a size parameter that is used to calculate a memory address. This address is then written to with controlled data. This can be abused by an attacker to corrupt memory and subsequently execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-07 - Vulnerability reported to vendor
- 2011-06-15 - Coordinated public release of advisory

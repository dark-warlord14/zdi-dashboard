# ZDI-10-163: Adobe Shockwave Director tSAC Chunk Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-163
- **ZDI-CAN:** ZDI-CAN-840
- **Date:** 2010-08-24
- **CVE:** CVE-2010-2874
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-163/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the undocumented tSAC RIFF chunk. By setting a specified field within this structure to NULL, the application fails to initialize an object pointer. This uninitialized pointer is later called which causes the application to jump into random heap memory. By crafting the applications memory state an attacker can utilize this issue to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-20.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-08-24 - Coordinated public release of advisory

# ZDI-10-089: Adobe Shockwave Director PAMI Chunk Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-089
- **ZDI-CAN:** ZDI-CAN-769
- **Date:** 2010-05-11
- **CVE:** CVE-2010-1292
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-089/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing Director files. When the application parses the pami RIFF chunk, it trusts an offset value and seeks into the file data. If provided with signed values in the data at the given offset, the process can be made to incorrectly calculate a pointer and operate on the data at it's location. This can be abused by an attacker to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-12.html

## Disclosure Timeline

- 2010-04-08 - Vulnerability reported to vendor
- 2010-05-11 - Coordinated public release of advisory

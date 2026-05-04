# ZDI-11-079: Adobe Shockwave Player 0xFFFFFF45 Record Count Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-079
- **ZDI-CAN:** ZDI-CAN-885
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0557
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 3D assets within a director movie. The routine responsible for parsing 3D record type 0xFFFFFF45 does not properly validate a count field within the structure. If this value is too large, the process can create a faulty allocation. Later, when the rendering routine attempts to use this buffer memory is corrupted. This can be abused by remote attackers to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-01.html

## Disclosure Timeline

- 2010-11-23 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory

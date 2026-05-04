# ZDI-10-088: Adobe Shockwave Player 0xFFFFFF49 Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-088
- **ZDI-CAN:** ZDI-CAN-723
- **Date:** 2010-05-11
- **CVE:** CVE-2010-1283
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Shockwave. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the code responsible for parsing 3D objects defined inside Director files. These files are essentially RIFF-based, but stored in big endian format. An undocumented 4-byte field within record type 0xFFFFFF49 can be modified to cause corruption of heap memory. This corruption can be used to modify function pointers and achieve remote code execution under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-12.html

## Disclosure Timeline

- 2010-03-12 - Vulnerability reported to vendor
- 2010-05-11 - Coordinated public release of advisory

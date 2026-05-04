# ZDI-11-211: Adobe Shockwave Shockwave 3d Asset.x32 DEMX Chunk 0xFFFFFF49 Field Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-211
- **ZDI-CAN:** ZDI-CAN-1195
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2113
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-211/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DEMX chunk inside Adobe's RIFF-based Director file format. The code within the Shockwave 3d Asset.x32 module does not properly check a size value used as the size for a malloc. The given size will wrap, causing a small buffer to be allocated. This can lead to memory corruption which can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-20 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory

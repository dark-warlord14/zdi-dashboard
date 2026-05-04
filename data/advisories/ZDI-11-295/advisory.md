# ZDI-11-295: Apple QuickTime FlashPix JPEG Tables Selector Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-295
- **ZDI-CAN:** ZDI-CAN-1312
- **Date:** 2011-10-18
- **CVE:** CVE-2011-3222
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-295/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles flashpix files. When a flashpix contains a tile that has a Compression Type 0x2 (JPEG) and an 'JPEG tables selector' value that is bigger then the global stream property 'Maximum JPEG table index', Quicktime will write outside the global JPEG table. This corruption could lead to remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5002

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-10-18 - Coordinated public release of advisory

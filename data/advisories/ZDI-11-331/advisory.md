# ZDI-11-331: RealNetwork RealPlayer MPG Width Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-331
- **ZDI-CAN:** ZDI-CAN-1294
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4259
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-331/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Realplayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way RealPlayer handles MPEG files. Realplayer parses the mpg file by doing a do while loop where it uses the width of the movie for the loop condition. However, it will substracts 1 from the width for every iteration of the loop and then compare it to 0. If the width of the movie was zero at the beginning the loop will run 0xFFFFFFFF times. This results in a memory corruption that can lead to remote code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-22 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory

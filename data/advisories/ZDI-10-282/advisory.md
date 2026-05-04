# ZDI-10-282: RealNetworks RealPlayer RealPix Server Header Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-282
- **ZDI-CAN:** ZDI-CAN-911
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4394
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-282/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within RealPlayer's parsing of RealPix files. If such a file contains an image tag pointing to a remote server, the player will attempt to fetch the remote file. When parsing the response from the web server, the process blindly copies the contents of the Server header into a fixed length heap buffer. If an attacker provides a large enough string, critical pointers can be overwritten allowing for arbitrary code execution under the context of the user running the player.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

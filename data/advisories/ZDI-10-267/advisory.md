# ZDI-10-267: RealNetworks RealPlayer Advanced Audio Coding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-267
- **ZDI-CAN:** ZDI-CAN-922
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4395
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-267/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's implementation of the Advanced Audio Coding compression format. When decoding a conditional component of a data block within an AAC frame the application will decompress lossy audio sample data outside the bounds of a buffer. This memory corruption can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-11-09 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

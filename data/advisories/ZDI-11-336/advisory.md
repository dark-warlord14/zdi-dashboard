# ZDI-11-336: RealNetworks RealPlayer Invalid Codec Name Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-336
- **ZDI-CAN:** ZDI-CAN-1278
- **Date:** 2011-11-28
- **CVE:** CVE-2011-4255
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-336/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when a user attempts to play a malicious video file containing a malformed codec name. When playing a malformed codec, the application will incorrectly free an object and then later attempt to use it by calling a virtual method pointer upon destruction. This can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-11-28 - Coordinated public release of advisory

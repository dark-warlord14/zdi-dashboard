# ZDI-12-051: RealNetworks RealPlayer RTSP SETUP Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-051
- **ZDI-CAN:** ZDI-CAN-1286
- **Date:** 2012-03-22
- **CVE:** CVE-2011-4254
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to the application mishandling an error that occurs when parsing an RTSP SETUP request. When an error occurs, the application will free a pointer to a linked list due to the stream being closed. Following this, the application will then attempt to access the freed element whilst traversing the list. This can lead to a use-after-free condition and can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2012-03-22 - Coordinated public release of advisory

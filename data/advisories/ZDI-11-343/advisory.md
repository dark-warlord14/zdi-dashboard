# ZDI-11-343: RealNetworks RealPlayer mp4arender esds channel count Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-343
- **ZDI-CAN:** ZDI-CAN-1351
- **Date:** 2011-12-07
- **CVE:** CVE-2011-4260
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-343/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Realplayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the mp4arender.dll module. If the channel count is altered inside the esds atom, the allocated buffer will be too small to support the decoded audio data, causing a heap overflow. This vulnerability can be leveraged to execute code under the context of the user running the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-28 - Vulnerability reported to vendor
- 2011-12-07 - Coordinated public release of advisory

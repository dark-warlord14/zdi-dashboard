# ZDI-12-046: RealNetworks RealPlayer Cook Codec Channel Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-046
- **ZDI-CAN:** ZDI-CAN-1276
- **Date:** 2012-03-20
- **CVE:** CVE-2011-4257
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses information out of the codec-specific data located within a media description header. When making space for audio-sample data, the application will allocate a static size. When decoding sample data into this buffer, an overflow will occur which can lead to memory corruption that can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2012-03-20 - Coordinated public release of advisory

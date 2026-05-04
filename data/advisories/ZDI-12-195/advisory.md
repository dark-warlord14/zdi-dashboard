# ZDI-12-195: RealNetworks RealPlayer ATRAC Sample Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-195
- **ZDI-CAN:** ZDI-CAN-1322
- **Date:** 2012-12-21
- **CVE:** CVE-2012-0928
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Andrzej Dyjak
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-195/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when the application attempts to decode an audio sample that is encoded with the ATRAC codec. While parsing sample data, the application will explicitly trust 2-bits as a loop counter which can be used to write outside the bounds of the target buffer. This can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/09072012_player/en/

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory

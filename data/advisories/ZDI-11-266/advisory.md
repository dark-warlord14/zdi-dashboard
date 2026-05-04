# ZDI-11-266: RealNetworks RealPlayer Advanced Audio Coding Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-266
- **ZDI-CAN:** ZDI-CAN-1122
- **Date:** 2011-08-16
- **CVE:** CVE-2011-2951
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Donato Ferrante Andrzej Dyjak
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-266/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to the application using a size defined in a header in order to allocate some number of bytes. When processing an AAC raw_data_frame, the application will use the product of the original length and a field inside one of its elements. During the copy operation, this length will be larger than the amount that was allocated for which will cause a buffer overflow and can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08162011_player/en/

## Disclosure Timeline

- 2011-05-13 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory

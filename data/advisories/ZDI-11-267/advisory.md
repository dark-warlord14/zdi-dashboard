# ZDI-11-267: RealNetworks Realplayer MP3 ID3 tags Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-267
- **ZDI-CAN:** ZDI-CAN-1136
- **Date:** 2011-08-16
- **CVE:** CVE-2011-2949
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-267/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Realplayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way RealPlayer handles ID3v2 Tags. RealPlayer creates a fixed size buffer for certain tags and will then populate them with the data from the file. It uses a call to WideCharToMultiByte to convert the data, but fails to take into account that converting a single wide char might result in more then two multi-byte chars. This causes more data to be written into the fixed buffer then anticipated resulting in a heap buffer overflow.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08162011_player/en/

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory

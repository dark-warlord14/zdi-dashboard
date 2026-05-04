# ZDI-12-048: RealNetworks RealPlayer VIDOBJ_START_CODE Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-048
- **ZDI-CAN:** ZDI-CAN-1368
- **Date:** 2012-03-22
- **CVE:** CVE-2012-0924
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a target must visit a malicious page or open a malicious file. The flaw exists within dmp4.dll, specifically the decoding of an MPEG stream. When encountering a VIDOBJ_START_CODE object the process inproperly validates the size of the destination buffer used for rendering. The contents of a decoded frame are copied to this region which can result in heap corruption if the decoded frame size exceeds the size of this region. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/02062012_player/en/

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-03-22 - Coordinated public release of advisory

# ZDI-12-049: RealNetworks RealPlayer RealAudio coded_frame_size Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-12-049
- **ZDI-CAN:** ZDI-CAN-1359
- **Date:** 2012-03-22
- **CVE:** CVE-2012-0927
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a target must visit a malicious page or open a malicious file. The flaw exists within cook.dll, specifically the handling of a RealAudio 2.0 file. When parsing the RA2 header a coded_frame_sz element is used to calculate the size for an allocation. This value is not properly verified before unpacking stream data into this new location. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/02062012_player/en/

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-03-22 - Coordinated public release of advisory

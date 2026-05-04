# ZDI-11-344: RealNetworks RealPlayer RV20 Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-344
- **ZDI-CAN:** ZDI-CAN-1304
- **Date:** 2011-12-07
- **CVE:** CVE-2011-4253
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put Andrzej Dyjak
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-344/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way that the application allocates space for parsing sample data encoded with the RV20 codec. After allocation, the application will partially fill the allocation with sample data. Upon usage of this sample data, the application will use the uninitialized data to calculate an index that is then written into. This can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2011-12-07 - Coordinated public release of advisory

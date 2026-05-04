# ZDI-12-085: RealNetworks RealPlayer dmp4 esds Width Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-085
- **ZDI-CAN:** ZDI-CAN-1360
- **Date:** 2012-06-06
- **CVE:** CVE-2011-4261
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-085/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dmp4 component. If the width value is altered inside the esds atom, arithmetic instructions within RealPlayer code can result in a loop counter wrapping to a large value. This can cause the loop to run too many times while operating on heap memory. By exploiting this condition, an attacker can corrupt memory and leverage that to execute code under the context of the user running the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-28 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory

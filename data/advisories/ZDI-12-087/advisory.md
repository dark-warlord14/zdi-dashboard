# ZDI-12-087: RealNetworks RealPlayer raac.dll stsz Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-087
- **ZDI-CAN:** ZDI-CAN-1352
- **Date:** 2012-06-06
- **CVE:** CVE-2011-4260
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-087/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the raac.dll module. By editing the stsz atom in the mp4 file data, an attacker could change a sample size to force a loop in raac.dll to loop too many times, causing heap corruption. This vulnerability can be leveraged to execute code under the context of the user running the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-28 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory

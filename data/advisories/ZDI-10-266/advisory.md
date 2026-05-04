# ZDI-10-266: RealNetworks RealPlayer Multi-Rate Audio Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-266
- **ZDI-CAN:** ZDI-CAN-473
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4375
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-266/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when parsing a RealMedia file containing a malformed multi-rate audio stream. The application explicitly trusts two 16-bit values in this data structure which are then used to calculate the size used for an allocation. When data is written to this allocated buffer, an overflow will occur which can lead to code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2009-04-15 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

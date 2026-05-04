# ZDI-10-270: RealNetworks RealPlayer ICY Protocol StreamTitle Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-270
- **ZDI-CAN:** ZDI-CAN-509
- **Date:** 2010-12-10
- **CVE:** CVE-2010-2997
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-270/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerability installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must open a malicious SHOUTcast Stream. The specific flaw exists in the processing of the StreamTitle tag in a SHOUTcast stream using the ICY protocol. A specially crafted string supplied as the property for the title can result in a failed allocation of heap memory. This then causes the freeing of critical pointers that are subsequently used after freeing. Successful exploitation of this vulnerability can lead to system compromise under the credentials of the currently logged in user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2009-06-25 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

# ZDI-10-166: RealNetworks RealPlayer Malformed IVR Object Index Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-166
- **ZDI-CAN:** ZDI-CAN-472
- **Date:** 2010-08-26
- **CVE:** CVE-2010-2996
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-166/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when parsing a RealMedia .IVR file containing a malformed data header. The application explicitly trusts an index in this data structure to seek into a list of objects. If one specifies an index outside the bounds of the array, the application will later dereference an object from the calculated pointer and then call it, leading to code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08262010_player/en/

## Disclosure Timeline

- 2009-04-15 - Vulnerability reported to vendor
- 2010-08-26 - Coordinated public release of advisory

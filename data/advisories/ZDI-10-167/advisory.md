# ZDI-10-167: RealNetworks RealPlayer FLV Parsing Multiple Integer Overflow Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-167
- **ZDI-CAN:** ZDI-CAN-620
- **Date:** 2010-08-26
- **CVE:** CVE-2010-3000
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sebastian Apelt, siberas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-167/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the module responsible for handling the FLV file format. While parsing the HX_FLV_META_AMF_TYPE_MIXEDARRAY and the HX_FLV_META_AMF_TYPE_ARRAY data types the ParseKnownType function makes two improper calculations that can force integers to wrap. A remote attacker can exploit these vulnerabilities to execute arbitrary code under the context of the user playing the file.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/08262010_player/en/

## Disclosure Timeline

- 2009-12-04 - Vulnerability reported to vendor
- 2010-08-26 - Coordinated public release of advisory

# ZDI-10-281: RealNetworks RealPlayer RMX Header Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-281
- **ZDI-CAN:** ZDI-CAN-913
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4391
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-281/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the applications support for parsing the RMX file format. When parsing the format, the application will explicitly trust 32-bits in a field used in the header for the allocation of an array. This can cause a buffer to be under-allocated and will cause a buffer overflow when initializing the array. This can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

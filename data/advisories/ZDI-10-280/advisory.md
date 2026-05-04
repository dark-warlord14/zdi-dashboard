# ZDI-10-280: RealNetworks RealPlayer ImageMap Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-280
- **ZDI-CAN:** ZDI-CAN-916
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4392
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Sebastian Apelt & Andreas Schmidt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-280/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application decodes data for a particular mime type within a RealMedia file. When decoding the data used for rendering, the application will use the length of a string in an addition used to calculate the size of a buffer. The application will zero-extend it and then allocate. Due to the addition, the result of the calculation can be greater than 16-bits, and when the typecast occurs the result will be smaller than expected. When initializing this buffer, a buffer overflow will occur which can allow for code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

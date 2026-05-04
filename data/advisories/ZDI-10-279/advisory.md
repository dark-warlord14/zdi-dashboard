# ZDI-10-279: RealNetworks RealPlayer Cook Codec Initialization Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-279
- **ZDI-CAN:** ZDI-CAN-881
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4389
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses cook-specific data used for initialization. The application will use a length in a copy without verifying it being larger than the destination buffer. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

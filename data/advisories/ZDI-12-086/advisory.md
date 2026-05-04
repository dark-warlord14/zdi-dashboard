# ZDI-12-086: RealNetworks RealPlayer rvrender RMFF Flags Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-086
- **ZDI-CAN:** ZDI-CAN-1361
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0922
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-086/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the rvrender module. When parsing an IVR file, the code within this module does not account for a negative value for the "RMFF 1.0 Flags" element within the input data. By providing a specially crafted file an attacker is able to achieve a program state that results in a function pointer value being retrieved from file data and subsequently called. This vulnerability can be leveraged to execute code under the context of the user running the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/02062012_player/en/

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory

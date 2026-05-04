# ZDI-12-050: RealNetworks RealPlayer mp4fformat rdrf Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-050
- **ZDI-CAN:** ZDI-CAN-1319
- **Date:** 2012-03-22
- **CVE:** CVE-2011-4262
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Realplayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within mp4fformat. The vulnerability resides in adding 1 to a trusted size value being taken out of the file data. The size value is then used in an operator_new call. This can be leveraged when the pointer returned from the operator_new is used in a memcpy as the destination buffer pointer. This vulnerability can result in remote code execution under the context of the user running the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-09-08 - Vulnerability reported to vendor
- 2012-03-22 - Coordinated public release of advisory

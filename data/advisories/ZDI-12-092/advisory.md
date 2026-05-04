# ZDI-12-092: RealNetworks RealPlayer QCELP Stream Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-092
- **ZDI-CAN:** ZDI-CAN-1313
- **Date:** 2012-06-08
- **CVE:** CVE-2011-4247
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-092/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way RealPlayer handles audio encoded with the QCELP codec. The codec allows you to specify the 'block_size' that is used. This size is used to create an allocation to hold the data, but a hardcoded blocksize is later used to copy data into that allocation. This could lead to remote code execution under the context of the current user.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-07-05 - Vulnerability reported to vendor
- 2012-06-08 - Coordinated public release of advisory

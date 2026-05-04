# ZDI-11-033: Realplayer vidplin.dll AVI Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-033
- **ZDI-CAN:** ZDI-CAN-801
- **Date:** 2011-01-27
- **CVE:** CVE-2010-4393
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Juan Pablo Lopez Yacubian
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Realnetworks Realplayer SP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the vidplin.dll module. A buffer is allocated according to the user supplied length value. User supplied data is then copied into the allocated buffer, without verifying length, allowing the data to be written past the bounds of the previously allocated buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user running RealPlayer.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/01272011_player/en/

## Disclosure Timeline

- 2010-09-14 - Vulnerability reported to vendor
- 2011-01-27 - Coordinated public release of advisory

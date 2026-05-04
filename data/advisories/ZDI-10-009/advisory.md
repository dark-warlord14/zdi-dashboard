# ZDI-10-009: RealNetworks RealPlayer IVR Format Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-009
- **ZDI-CAN:** ZDI-CAN-318
- **Date:** 2010-01-21
- **CVE:** CVE-2009-0376
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** John Rambo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-009/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within RealPlayer's parsing of IVR files. The process trusts size values present in the file and uses them unsafely in various file I/O and memory allocation operations. A specially crafted file can cause memory overflows to occur leading to arbitrary code execution under the context of the user running the player.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/01192010_player/en/

## Disclosure Timeline

- 2008-04-16 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory

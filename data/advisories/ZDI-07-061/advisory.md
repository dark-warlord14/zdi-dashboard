# ZDI-07-061: RealNetworks RealPlayer SWF Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-061
- **ZDI-CAN:** ZDI-CAN-141
- **Date:** 2007-11-02
- **CVE:** CVE-2007-2263
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-061/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of the RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in RealPlayer's parsing of SWF files. The SWF rendering DLL RealPlayer uses fails to properly handle malformed record headers leading to an exploitable overflow. An attacker could exploit this vulnerability using an ActiveX control {CFCDAA03-8BE4-11cf-B84B-0020AFBBCCFA} and embedding the malicious swf file in the page or by convincing an affected user to directly open a SWF file using RealPlayer.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10252007_player/en/

## Disclosure Timeline

- 2007-01-17 - Vulnerability reported to vendor
- 2007-11-02 - Coordinated public release of advisory

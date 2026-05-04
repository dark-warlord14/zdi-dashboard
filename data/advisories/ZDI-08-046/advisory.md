# ZDI-08-046: RealNetworks RealPlayer Library File Deletion Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-046
- **ZDI-CAN:** ZDI-CAN-231
- **Date:** 2008-07-25
- **CVE:** CVE-2008-3066
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of the RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in RealPlayer's rjbdll.dll module when handling the deletion of media library files. An attacker could exploit this vulnerability using an ActiveX control {FDC7A535-4070-4B92-A0EA-D9994BCC0DC5} to import a vulnerable file into the user's media library. Upon deletion of this file, an exploitable stack based buffer overflow can be triggered.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/07252008_player/en/

## Disclosure Timeline

- 2007-11-02 - Vulnerability reported to vendor
- 2008-07-25 - Coordinated public release of advisory

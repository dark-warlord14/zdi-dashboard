# ZDI-10-210: RealNetworks RealPlayer ActiveX Control CDDA URI Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-210
- **ZDI-CAN:** ZDI-CAN-600
- **Date:** 2010-10-15
- **CVE:** CVE-2010-3747
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** CHkr_D591
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-210/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during the parsing of long CDDA URIs due to a failure to initialize a particular component of an object. The application will later call a method in the object leading to the uninitialized pointer being called. If an attacker can place data they control at the uninitialized location, the application will call malicious pointer which can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/10152010_player/en/

## Disclosure Timeline

- 2009-11-24 - Vulnerability reported to vendor
- 2010-10-15 - Coordinated public release of advisory

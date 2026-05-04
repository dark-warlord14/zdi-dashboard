# ZDI-11-076: RealNetworks Real Player Predictable Temporary File Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-076
- **ZDI-CAN:** ZDI-CAN-849
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0694
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Eduardo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the temporary file naming scheme used for storage of references to Real Media files. This easily predictable temporary filename can be brute forced and used in combination with the OpenURLinPlayerBrowser function available in classid:FDC7A535-4070-4B92-A0EA-D9994BCC0DC5 to execute the file. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/02082011_player/en/

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory

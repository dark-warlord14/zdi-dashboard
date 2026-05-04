# ZDI-10-275: RealNetworks RealPlayer Cross-Zone Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-275
- **ZDI-CAN:** ZDI-CAN-771
- **Date:** 2010-12-10
- **CVE:** CVE-2010-4396
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-275/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is requires in that a target must navigate to a malicious page. The specific flaw exists within the HandleAction method of the RealPlayer ActiveX control with CLSID FDC7A535-4070-4B92-A0EA-D9994BCC0DC5. The vulnerable action that can be invoked via this control is NavigateToURL. If NavigateToURL can be pointed to a controlled file on the user's system, RealPlayer can be made to execute scripts in the Local Zone. To accomplish this, a malicious attacker can force a download of a skin file to a predictable location and then point NavigateToURL at it thus achieving remote code execution under the context of the user running RealPlayer.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/12102010_player/en/

## Disclosure Timeline

- 2010-05-12 - Vulnerability reported to vendor
- 2010-12-10 - Coordinated public release of advisory

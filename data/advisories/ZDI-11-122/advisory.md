# ZDI-11-122: RealNetworks RealPlayer OpenURLInDefaultBrowser Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-122
- **ZDI-CAN:** ZDI-CAN-1016
- **Date:** 2011-04-12
- **CVE:** CVE-2011-1426
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl ) Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-122/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks RealPlayer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within RealPlayer exposes a method called OpenURLInDefaultBrowser() that can be accessed through RealPlayer's internal browser. When this method is called, it will open and execute the first parameter based on the operating system's default handler for the filetype. An attacker can reach RealPlayer's internal browser by utilizing a specially crafted .rnx file. This can be leveraged to execute arbitrary code under the context of the user invoking RealPlayer.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/04122011_player/en/

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory

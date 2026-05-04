# ZDI-07-047: Microsoft Windows Media Player Malformed Skin Header Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-047
- **ZDI-CAN:** ZDI-CAN-198
- **Date:** 2007-08-14
- **CVE:** CVE-2007-3035
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows Media Player 7, Windows Media Player 9, Windows Media Player 10, Windows Media Player 11
- **Credit:** Piotr Bania
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-047/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists while decompressing skin files (.WMZ and .WMD) with malformed headers. During this process the malformed values are used to improperly calculate data which can later allow an attacker to execute code under the rights of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS07-047.mspx

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2007-08-14 - Coordinated public release of advisory

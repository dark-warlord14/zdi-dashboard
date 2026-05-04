# ZDI-10-010: RealNetworks RealPlayer Skin Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-010
- **ZDI-CAN:** ZDI-CAN-421
- **Date:** 2010-01-21
- **CVE:** CVE-2009-4246
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Peter Vreugdenhil (security@petervreugdenhil.nl)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-010/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealNetworks RealPlayer. User interaction is required in that a user must visit a malicious website or open a malicious file and accept a dialog to switch player skins. The specific flaw exists during parsing of malformed RealPlayer .RJS skin files. While loading a skin the application copies certain variable length fields from the extracted file named web.xmb into a statically sized buffer. By crafting these fields appropriately an attack can cause the process to overflow the buffer. This can be leveraged to execute arbitrary code with the privileges of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/01192010_player/en/

## Disclosure Timeline

- 2009-01-15 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory

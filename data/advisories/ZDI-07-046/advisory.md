# ZDI-07-046: Microsoft Windows Media Player Skin Parsing Size Mismatch Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-046
- **ZDI-CAN:** ZDI-CAN-182
- **Date:** 2007-08-14
- **CVE:** CVE-2007-3037
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows Media Player 7, Windows Media Player 9, Windows Media Player 10, Windows Media Player 11
- **Credit:** Piotr Bania
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-046/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of malformed skin files (WMZ). A size compressed / decompressed size mismatch can result in an under allocated heap buffer which can be leveraged by an attacker to eventually execute arbitrary code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS07-047.mspx

## Disclosure Timeline

- 2007-03-19 - Vulnerability reported to vendor
- 2007-08-14 - Coordinated public release of advisory

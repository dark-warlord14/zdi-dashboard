# ZDI-19-545: Microsoft Windows gdiplus Font Parsing Off-By-One Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-545
- **ZDI-CAN:** ZDI-CAN-8031
- **Date:** 2019-06-11
- **CVE:** CVE-2019-0968
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-545/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of font files in the gdiplus library. Crafted data in a font file can trigger an off-by-one error before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0968

## Disclosure Timeline

- 2019-02-21 - Vulnerability reported to vendor
- 2019-06-11 - Coordinated public release of advisory

# ZDI-20-1003: Microsoft Windows fontdrvhost Font Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1003
- **ZDI-CAN:** ZDI-CAN-10816
- **Date:** 2020-08-14
- **CVE:** CVE-2020-1561
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TTF fonts. A crafted TTF font can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the user-mode font driver process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1561

## Disclosure Timeline

- 2020-05-07 - Vulnerability reported to vendor
- 2020-08-14 - Coordinated public release of advisory

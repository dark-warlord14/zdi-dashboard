# ZDI-20-1405: Apple macOS libFontParser TwOFFStream TTF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1405
- **ZDI-CAN:** ZDI-CAN-11801
- **Date:** 2020-12-08
- **CVE:** CVE-2020-27931
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Junzhi Lu of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1405/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the libFontParser library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of TTF fonts. Crafted data in a TTF font can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This issue was addressed in macOS Big Sur 11.0.1.

## Disclosure Timeline

- 2020-08-26 - Vulnerability reported to vendor
- 2020-12-08 - Coordinated public release of advisory

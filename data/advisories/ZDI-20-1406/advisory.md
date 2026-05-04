# ZDI-20-1406: Apple macOS CoreText MorxLigatureSubtableBuilder TTF Parsing Out-of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1406
- **ZDI-CAN:** ZDI-CAN-11828
- **Date:** 2020-12-08
- **CVE:** CVE-2020-9999
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Junzhi Lu of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1406/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the CoreText library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of TTF fonts. Crafted data in a TTF file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This issue was addressed in macOS Big Sur 11.0.1.

## Disclosure Timeline

- 2020-08-26 - Vulnerability reported to vendor
- 2020-12-08 - Coordinated public release of advisory

# ZDI-20-1404: Apple macOS libFontParser TTF Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1404
- **ZDI-CAN:** ZDI-CAN-11598
- **Date:** 2020-12-08
- **CVE:** CVE-2020-27952
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Junzhi Lu of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1404/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the libFontParser library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of TTF fonts. Crafted data in a TTF font can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This issue was addressed in macOS Big Sur 11.0.1.

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-12-08 - Coordinated public release of advisory

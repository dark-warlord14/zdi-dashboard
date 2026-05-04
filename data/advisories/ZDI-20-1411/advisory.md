# ZDI-20-1411: Apple macOS libFontParser TTF Font Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1411
- **ZDI-CAN:** ZDI-CAN-11588
- **Date:** 2020-12-09
- **CVE:** CVE-2020-9956
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin & Junzhi Lu of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1411/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the RenderGlyph function in libFontParser. Crafted data in a TTF font can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This issue was addressed in macOS Big Sur 11.0.1 and iOS 14.

## Disclosure Timeline

- 2020-07-29 - Vulnerability reported to vendor
- 2020-12-09 - Coordinated public release of advisory

# ZDI-22-1295: Apple macOS TIFF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1295
- **ZDI-CAN:** ZDI-CAN-16749
- **Date:** 2022-09-21
- **CVE:** N/A
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1295/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the CoreGraphics framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of TIFF images. Crafted data in a TIFF image can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

According to Apple, ZDI-CAN-16749 was addressed in macOS Monterey 12.5 and iOS & iPadOS 15.6. Apple informed ZDI they would assign a CVE, but never followed through.

## Disclosure Timeline

- 2022-03-04 - Vulnerability reported to vendor
- 2022-09-21 - Coordinated public release of advisory

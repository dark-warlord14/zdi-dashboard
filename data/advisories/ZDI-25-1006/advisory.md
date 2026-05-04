# ZDI-25-1006: Apple macOS CoreText Font Glyph Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1006
- **ZDI-CAN:** ZDI-CAN-27796
- **Date:** 2025-11-13
- **CVE:** CVE-2025-43445
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Hossein Lotfi (@hosselot) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of font glyphs in the CoreText framework. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125635

## Disclosure Timeline

- 2025-07-29 - Vulnerability reported to vendor
- 2025-11-13 - Coordinated public release of advisory
- 2025-11-13 - Advisory Updated

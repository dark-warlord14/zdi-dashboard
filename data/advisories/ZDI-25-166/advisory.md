# ZDI-25-166: Apple macOS libFontParser Glyph Mapping Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-166
- **ZDI-CAN:** ZDI-CAN-25338
- **Date:** 2025-03-18
- **CVE:** CVE-2024-54486
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Hossein Lotfi (@hosselot) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-166/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the libFontParser library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementation of glyph mapping. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/121839

## Disclosure Timeline

- 2024-09-10 - Vulnerability reported to vendor
- 2025-03-18 - Coordinated public release of advisory
- 2025-03-18 - Advisory Updated

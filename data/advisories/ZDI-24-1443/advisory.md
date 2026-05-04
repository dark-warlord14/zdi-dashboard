# ZDI-24-1443: Apple macOS ImageIO JP2 Image Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1443
- **ZDI-CAN:** ZDI-CAN-23979
- **Date:** 2024-10-31
- **CVE:** CVE-2024-44215
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1443/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a JP2 image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/121564

## Disclosure Timeline

- 2024-06-28 - Vulnerability reported to vendor
- 2024-10-31 - Coordinated public release of advisory
- 2025-03-06 - Advisory Updated

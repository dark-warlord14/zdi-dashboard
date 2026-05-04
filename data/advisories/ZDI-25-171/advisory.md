# ZDI-25-171: Apple macOS ImageIO Pixel Conversion Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-171
- **ZDI-CAN:** ZDI-CAN-25242
- **Date:** 2025-03-18
- **CVE:** CVE-2024-54500
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-171/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the handling of pixel conversion. Crafted data in a PVR image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/121839

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-03-18 - Coordinated public release of advisory
- 2025-03-18 - Advisory Updated

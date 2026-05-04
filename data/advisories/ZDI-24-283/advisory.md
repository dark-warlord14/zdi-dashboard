# ZDI-24-283: Apple macOS JP2 Image Parsing Uninitialized Pointer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-283
- **ZDI-CAN:** ZDI-CAN-22250
- **Date:** 2024-03-11
- **CVE:** CVE-2024-23257
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-283/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a JP2 image can trigger access to a pointer prior to initialization. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT214084

## Disclosure Timeline

- 2023-11-01 - Vulnerability reported to vendor
- 2024-03-11 - Coordinated public release of advisory
- 2025-03-06 - Advisory Updated

# ZDI-24-1283: Apple macOS ImageIO JP2 File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1283
- **ZDI-CAN:** ZDI-CAN-24570
- **Date:** 2024-09-25
- **CVE:** CVE-2024-44176
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1283/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a JP2 image can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/121247

## Disclosure Timeline

- 2024-08-06 - Vulnerability reported to vendor
- 2024-09-25 - Coordinated public release of advisory
- 2025-03-06 - Advisory Updated

# ZDI-24-1313: Apple macOS ImageIO PSD File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1313
- **ZDI-CAN:** ZDI-CAN-24194
- **Date:** 2024-10-02
- **CVE:** CVE-2024-40777
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1313/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a PSD file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT214119

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-10-02 - Coordinated public release of advisory
- 2025-03-06 - Advisory Updated

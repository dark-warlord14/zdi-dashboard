# ZDI-26-175: Apple macOS ImageIO SGI File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-175
- **ZDI-CAN:** ZDI-CAN-28081
- **Date:** 2026-03-10
- **CVE:** CVE-2026-20634
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** George Karchemsky (@gkarchemsky)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-175/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a SGI image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/126347

## Disclosure Timeline

- 2025-11-05 - Vulnerability reported to vendor
- 2026-03-10 - Coordinated public release of advisory
- 2026-03-10 - Advisory Updated

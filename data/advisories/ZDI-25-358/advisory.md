# ZDI-25-358: (Pwn2Own) Sony XAV-AX8500 Bluetooth ERTM Channel Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-358
- **ZDI-CAN:** ZDI-CAN-26285
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5820
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Sony
- **Affected Products:** XAV-AX8500
- **Credit:** Mikhail Evdokimov (@konatabrk) from PCAutomotive
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-358/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected Sony XAV-AX8500 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of Bluetooth ERTM channel communication. The issue results from improper channel data initialization. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Sony has issued an update to correct this vulnerability. More details can be found at: https://www.sony.com/electronics/support/mobile-cd-players-digital-media-players-xav-series/xav-ax8500/software/00344092

## Disclosure Timeline

- 2025-01-30 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

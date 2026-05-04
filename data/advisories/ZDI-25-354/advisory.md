# ZDI-25-354: (Pwn2Own) Sony XAV-AX8500 Bluetooth L2CAP Protocol Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-354
- **ZDI-CAN:** ZDI-CAN-26286
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5477
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sony
- **Affected Products:** XAV-AX8500
- **Credit:** Mikhail Evdokimov (@konatabrk) from PCAutomotive
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-354/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Sony XAV-AX8500 devices. An attacker must first obtain the ability to pair a malicious Bluetooth device with the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the Bluetooth L2CAP protocol. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the elysian-bt-service process.

## Additional Details

Sony has issued an update to correct this vulnerability. More details can be found at: https://www.sony.com/electronics/support/mobile-cd-players-digital-media-players-xav-series/xav-ax8500/software/00344092

## Disclosure Timeline

- 2025-01-30 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

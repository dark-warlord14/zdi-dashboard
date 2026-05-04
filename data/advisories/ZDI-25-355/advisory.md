# ZDI-25-355: (Pwn2Own) Sony XAV-AX8500 Bluetooth SDP Protocol Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-355
- **ZDI-CAN:** ZDI-CAN-26288
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5478
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sony
- **Affected Products:** XAV-AX8500
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-355/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Sony XAV-AX8500 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the Bluetooth SDP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Sony has issued an update to correct this vulnerability. More details can be found at: https://www.sony.com/electronics/support/mobile-cd-players-digital-media-players-xav-series/xav-ax8500/software/00344092

## Disclosure Timeline

- 2025-01-28 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

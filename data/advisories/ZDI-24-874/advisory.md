# ZDI-24-874: (Pwn2Own) Sony XAV-AX5500 Insufficient Firmware Update Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-874
- **ZDI-CAN:** ZDI-CAN-22939
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23922
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sony
- **Affected Products:** XAV-AX5500
- **Credit:** Tobias Scharnowski (@ScepticCTF), Felix Buchmann
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-874/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Sony XAV-AX5500 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of software updates. The issue results from the lack of proper validation of software update packages. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Sony has issued an update to correct this vulnerability. More details can be found at: https://www.sony.com/electronics/support/mobile-cd-players-digital-media-players-xav-series/xav-ax5500/software/00274156

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

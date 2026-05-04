# ZDI-24-875: (Pwn2Own) Sony XAV-AX5500 WMV/ASF Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-875
- **ZDI-CAN:** ZDI-CAN-22994
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23934
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sony
- **Affected Products:** XAV-AX5500
- **Credit:** Gary Wang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-875/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sony XAV-AX5500 devices. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WMV/ASF files. A crafted Extended Content Description Object in a WMV media file can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Sony has issued an update to correct this vulnerability. More details can be found at: https://www.sony.com/electronics/support/mobile-cd-players-digital-media-players-xav-series/xav-ax5500/software/00274156

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

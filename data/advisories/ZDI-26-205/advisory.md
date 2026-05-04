# ZDI-26-205: (Pwn2Own) Canon imageCLASS MF654Cdw PJCC Request Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-205
- **ZDI-CAN:** ZDI-CAN-28334
- **Date:** 2026-03-16
- **CVE:** CVE-2025-14234
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF654Cdw
- **Credit:** Team ANHTUD
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-205/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF654Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CADM service, which listens on TCP port 9013 by default. A crafted font in a PJCC request can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security/

## Disclosure Timeline

- 2025-11-11 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

# ZDI-26-206: (Pwn2Own) Canon imageCLASS MF654Cdw TTF Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-206
- **ZDI-CAN:** ZDI-CAN-28349
- **Date:** 2026-03-16
- **CVE:** CVE-2025-14235
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF654Cdw
- **Credit:** PHP HOOLIGANS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-206/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF654Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within parsing of TrueType fonts. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security/

## Disclosure Timeline

- 2025-11-11 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

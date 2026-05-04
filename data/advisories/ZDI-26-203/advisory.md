# ZDI-26-203: (Pwn2Own) Canon imageCLASS MF654Cdw XML SOAP Request Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-203
- **ZDI-CAN:** ZDI-CAN-28346
- **Date:** 2026-03-16
- **CVE:** CVE-2025-14231
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF654Cdw
- **Credit:** Nguyễn Hoàng Thạch, Gerrard Tai, Cherie-Anne Lee, Tan Ze Jian, Lin Ze Wei of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-203/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF654Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of SOAP requests. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security/

## Disclosure Timeline

- 2025-11-11 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

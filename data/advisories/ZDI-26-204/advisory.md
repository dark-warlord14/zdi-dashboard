# ZDI-26-204: (Pwn2Own) Canon imageCLASS MF654Cdw XPS Parser Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-204
- **ZDI-CAN:** ZDI-CAN-28268
- **Date:** 2026-03-16
- **CVE:** CVE-2025-14232
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF654Cdw
- **Credit:** SHIMIZU Yutaro (@shift_crops) of GMO Cybersecurity by Ierae, Inc.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-204/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF654Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of XPS files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security/

## Disclosure Timeline

- 2025-11-11 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

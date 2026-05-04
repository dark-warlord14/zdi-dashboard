# ZDI-25-074: (Pwn2Own) Canon imageCLASS MF656Cdw TIF File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-074
- **ZDI-CAN:** ZDI-CAN-25592
- **Date:** 2025-01-31
- **CVE:** CVE-2024-12648
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF656Cdw
- **Credit:** Alain Rodel, Neodyme AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-074/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF656Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of TIF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security/#news

## Disclosure Timeline

- 2025-01-31 - Vulnerability reported to vendor
- 2025-01-31 - Coordinated public release of advisory
- 2025-01-31 - Advisory Updated

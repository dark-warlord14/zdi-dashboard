# ZDI-25-075: (Pwn2Own) Canon imageCLASS MF656Cdw TTF Parsing Write-What-Where Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-075
- **ZDI-CAN:** ZDI-CAN-25622
- **Date:** 2025-01-31
- **CVE:** CVE-2024-12649
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF656Cdw
- **Credit:** PHP Hooligans / Midnight Blue
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-075/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF656Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within parsing of TrueType fonts. The issue results from the lack of proper validation of user-supplied data, which can result in a write-what-where condition. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security/#news

## Disclosure Timeline

- 2024-12-16 - Vulnerability reported to vendor
- 2025-01-31 - Coordinated public release of advisory
- 2025-01-31 - Advisory Updated

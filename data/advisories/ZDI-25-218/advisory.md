# ZDI-25-218: (Pwn2Own) Lexmark CX331adwe JPEG2000 Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-218
- **ZDI-CAN:** ZDI-CAN-25621
- **Date:** 2025-04-09
- **CVE:** CVE-2024-11345
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** PHP Hooligans / Midnight Blue
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-218/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark CX331adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of JPEG2000 files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the pagemaker user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://support.lexmark.com/content/dam/support/collateral/security-alerts/CVE-2024-11345.pdf

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated

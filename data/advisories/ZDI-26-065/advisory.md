# ZDI-26-065: (Pwn2Own) Lexmark CX532adwe usecmap Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-065
- **ZDI-CAN:** ZDI-CAN-28328
- **Date:** 2026-02-05
- **CVE:** CVE-2025-65080
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX532adwe
- **Credit:** Chris Anastasio @mufinnnnnnn Fabius Watson @FabiusArtrel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-065/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark CX532adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the usecmap method. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the pagemaker user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://www.lexmark.com/content/dam/support/collateral/security-alerts/CVE-2025-65080.pdf

## Disclosure Timeline

- 2025-11-06 - Vulnerability reported to vendor
- 2026-02-05 - Coordinated public release of advisory
- 2026-02-05 - Advisory Updated

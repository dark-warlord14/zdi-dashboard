# ZDI-26-064: (Pwn2Own) Lexmark CX532adwe execuserobject Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-064
- **ZDI-CAN:** ZDI-CAN-28341
- **Date:** 2026-02-05
- **CVE:** CVE-2025-65081
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX532adwe
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-064/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark CX532adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the execuserobject function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the pagemaker user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://www.lexmark.com/content/dam/support/collateral/security-alerts/CVE-2025-65081.pdf

## Disclosure Timeline

- 2025-11-06 - Vulnerability reported to vendor
- 2026-02-05 - Coordinated public release of advisory
- 2026-02-18 - Advisory Updated

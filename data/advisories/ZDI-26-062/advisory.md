# ZDI-26-062: (Pwn2Own) Lexmark CX532adwe esfhelper Untrusted Search Path Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-062
- **ZDI-CAN:** ZDI-CAN-28477
- **Date:** 2026-02-05
- **CVE:** CVE-2025-65078
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX532adwe
- **Credit:** Interrupt Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-062/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Lexmark CX532adwe printers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the esfhelper binary. The issue results from executing a program from an untrusted location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://www.lexmark.com/content/dam/support/collateral/security-alerts/CVE-2025-65083.pdf

## Disclosure Timeline

- 2025-11-05 - Vulnerability reported to vendor
- 2026-02-05 - Coordinated public release of advisory
- 2026-02-10 - Advisory Updated

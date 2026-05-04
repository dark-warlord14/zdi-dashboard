# ZDI-25-624: (Pwn2Own) Phoenix Contact CHARX SEC-3100 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-624
- **ZDI-CAN:** ZDI-CAN-23328
- **Date:** 2025-07-21
- **CVE:** CVE-2024-25995
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Alex Olson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-624/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the defaultroutemetric parameter to the config service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://certvde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2025-07-21 - Coordinated public release of advisory
- 2025-07-21 - Advisory Updated

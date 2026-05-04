# ZDI-25-264: (Pwn2Own) Tesla Model S Iris Modem ql_atfwd Command Injection Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-264
- **ZDI-CAN:** ZDI-CAN-23201
- **Date:** 2025-04-30
- **CVE:** CVE-2024-6032
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model S
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-264/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected Tesla Model S vehicles. An attacker must first obtain the ability to execute code on the target system in order to exploit this vulnerability. The specific flaw exists within the ql_atfwd process. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code on the target modem in the context of root.

## Additional Details

Fixed in Firmware Version 2024.8

## Disclosure Timeline

- 2024-02-28 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated

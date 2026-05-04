# ZDI-25-260: (Pwn2Own) Tesla Model S Iris Modem Race Condition Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-260
- **ZDI-CAN:** ZDI-CAN-23197
- **Date:** 2025-04-30
- **CVE:** CVE-2024-6029
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Tesla
- **Affected Products:** Model S
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-260/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass the firewall on the Iris modem in affected Tesla Model S vehicles. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firewall service. The issue results from a failure to obtain the xtables lock. An attacker can leverage this vulnerability to bypass firewall rules.

## Additional Details

Fixed in Firmware Version 2024.2.3

## Disclosure Timeline

- 2024-02-28 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated

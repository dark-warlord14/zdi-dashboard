# ZDI-24-1152: Phoenix Contact CHARX SEC-3100 Improper Access Control Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1152
- **ZDI-CAN:** ZDI-CAN-23499
- **Date:** 2024-08-20
- **CVE:** CVE-2024-3913
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Alex Olson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1152/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firewall. The issue results from incorrect ordering and synchronization of services during startup. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-022/

## Disclosure Timeline

- 2024-03-15 - Vulnerability reported to vendor
- 2024-08-20 - Coordinated public release of advisory
- 2024-08-20 - Advisory Updated

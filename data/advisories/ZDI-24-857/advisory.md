# ZDI-24-857: (Pwn2Own) Phoenix Contact CHARX SEC-3100 Improper Access Control Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-857
- **ZDI-CAN:** ZDI-CAN-23221
- **Date:** 2024-06-21
- **CVE:** CVE-2024-25996
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Tobias Scharnowski (@ScepticCTF), Felix Buchmann
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-857/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass firewall rules and access another interface on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of firewall rules. The issue results from the use of rules that filter inbound traffic on the basis of the source port. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

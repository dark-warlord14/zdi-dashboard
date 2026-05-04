# ZDI-25-623: (Pwn2Own) Phoenix Contact CHARX SEC-3150 Origin Validation Error Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-623
- **ZDI-CAN:** ZDI-CAN-26332
- **Date:** 2025-07-21
- **CVE:** CVE-2025-25270
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3150
- **Credit:** Tobias Scharnowski, Felix Buchmann, and Kristian Covic of fuzzware.io
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-623/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass firewall rules and access another interface on affected installations of Phoenix Contact CHARX SEC-3150 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of firewall rules. The issue results from the use of rules that filter outbound traffic on the basis of the source port. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://certvde.com/en/advisories/VDE-2025-019/

## Disclosure Timeline

- 2025-05-12 - Vulnerability reported to vendor
- 2025-07-21 - Coordinated public release of advisory
- 2025-07-21 - Advisory Updated

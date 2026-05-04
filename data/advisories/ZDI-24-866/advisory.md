# ZDI-24-866: (Pwn2Own) Phoenix Contact CHARX SEC-3100 CANopenDevice Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-866
- **ZDI-CAN:** ZDI-CAN-24095
- **Date:** 2024-06-21
- **CVE:** CVE-2024-26004
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** RET2 Systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-866/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of CANopenDevice objects. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-05-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

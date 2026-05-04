# ZDI-25-212: (Pwn2Own) Synology BeeStation BST150-4T Improper Authentication Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-212
- **ZDI-CAN:** ZDI-CAN-25658
- **Date:** 2025-04-09
- **CVE:** CVE-2024-50630
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation BST150-4T
- **Credit:** Pumpkin Chang (@u1f383) and Orange Tsai (@orange_8361) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-212/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Synology BeeStation BST150-4T devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the syncd authentication handler. The issue results from incorrect implementation of an authentication algorithm. An attacker can leverage this in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_21

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated

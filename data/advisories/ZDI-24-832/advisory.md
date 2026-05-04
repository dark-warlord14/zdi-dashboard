# ZDI-24-832: (Pwn2Own) Synology RT6600ax Improper Access Control Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-832
- **ZDI-CAN:** ZDI-CAN-22430
- **Date:** 2024-07-11
- **CVE:** CVE-2024-39347
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** RT6600ax
- **Credit:** Tri and Bien Pham (@bienpnn) from Team Orca of Sea Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-832/
## Vulnerability Details

This vulnerability allows remote attackers to bypass firewall rules and access the LAN interface on affected installations of Synology RT6600ax routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of firewall rules. The issue results from improper access control after the initial setup. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-id/security/advisory/Synology_SA_23_16

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-07-11 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

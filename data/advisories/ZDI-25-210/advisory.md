# ZDI-25-210: (Pwn2Own) Synology BeeStation BST150-4T Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-210
- **ZDI-CAN:** ZDI-CAN-25662
- **Date:** 2025-04-09
- **CVE:** CVE-2024-10445
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation BST150-4T
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-210/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology BeeStation BST150-4T devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of tar archives. A crafted tar archive can trigger the creation of symlinks to arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_20

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated

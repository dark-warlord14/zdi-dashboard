# ZDI-25-269: (Pwn2Own) Synology BeeStation BST150-4T Unnecessary Privileges Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-269
- **ZDI-CAN:** ZDI-CAN-25663
- **Date:** 2025-05-01
- **CVE:** CVE-2024-10445
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation BST150-4T
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-269/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology BeeStation BST150-4T devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of file commands. The specific flaw exists within the handling of files as the root user. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_20

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-05-01 - Coordinated public release of advisory
- 2025-05-01 - Advisory Updated

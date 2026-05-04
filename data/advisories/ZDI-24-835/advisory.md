# ZDI-24-835: (Pwn2Own) Synology BC500 Protection Mechanism Failure Software Downgrade Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-835
- **ZDI-CAN:** ZDI-CAN-22460
- **Date:** 2024-07-11
- **CVE:** CVE-2024-39352
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BC500
- **Credit:** Romain JOUET (@JouetR), Baptiste MOINE (@Creased_) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-835/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to downgrade Synology software on affected installations of Synology BC500 cameras. Authentication is required to exploit this vulnerability. The specific flaw exists within the update functionality. The issue results from the lack of proper validation of version information before performing an update. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-id/security/advisory/Synology_SA_23_15

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-07-11 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

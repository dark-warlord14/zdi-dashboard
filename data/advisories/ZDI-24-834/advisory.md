# ZDI-24-834: (Pwn2Own) Synology BC500 Improper Compartmentalization Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-834
- **ZDI-CAN:** ZDI-CAN-22311
- **Date:** 2024-07-11
- **CVE:** CVE-2024-39350
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BC500
- **Credit:** Romain JOUET (@JouetR), Baptiste MOINE (@Creased_) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-834/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Synology BC500 cameras. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of user accounts. The issue results from the lack of proper configuration for non-admin accounts. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-id/security/advisory/Synology_SA_23_15

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-07-11 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

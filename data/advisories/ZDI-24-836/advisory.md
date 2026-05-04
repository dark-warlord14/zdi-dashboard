# ZDI-24-836: (Pwn2Own) Synology BC500 update_ntp_config Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-836
- **ZDI-CAN:** ZDI-CAN-22461
- **Date:** 2024-06-21
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BC500
- **Credit:** Romain JOUET (@JouetR), Baptiste MOINE (@Creased_) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-836/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology BC500 IP cameras. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the server parameter provided to the syno-api handler. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-id/security/advisory/Synology_SA_23_15

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

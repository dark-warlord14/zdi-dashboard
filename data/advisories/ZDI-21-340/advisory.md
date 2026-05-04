# ZDI-21-340: (Pwn2Own) Synology DiskStation Manager iscsi_snapshot_comm_core Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-340
- **ZDI-CAN:** ZDI-CAN-13476
- **Date:** 2021-03-22
- **CVE:** CVE-2021-27646
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-340/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Synology DS418play. Authentication is not required to exploit this vulnerability. The specific flaw exists within the iscsi_snapshot_comm_core service. The issue results from the lack of proper locking when performing operations on an object, which can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the current process.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/zh-hk/security/advisory/Synology_SA_20_26

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2021-03-22 - Coordinated public release of advisory
- 2021-05-24 - Advisory Updated

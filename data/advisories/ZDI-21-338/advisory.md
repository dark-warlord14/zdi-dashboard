# ZDI-21-338: (Pwn2Own) Synology DiskStation Manager iscsi_snapshot_comm_core Race Condition Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-338
- **ZDI-CAN:** ZDI-CAN-12305
- **Date:** 2021-03-18
- **CVE:** CVE-2021-26569
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-338/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Synology DS418play. Authentication is not required to exploit this vulnerability. The specific flaw exists within the iscsi_snapshot_comm_core service. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the current process.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/zh-hk/security/advisory/Synology_SA_20_26

## Disclosure Timeline

- 2020-11-07 - Vulnerability reported to vendor
- 2021-03-18 - Coordinated public release of advisory
- 2021-05-24 - Advisory Updated

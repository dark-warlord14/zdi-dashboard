# ZDI-25-208: (Pwn2Own) Synology DiskStation DS1823xs+ Replication Service Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-208
- **ZDI-CAN:** ZDI-CAN-25607
- **Date:** 2025-04-09
- **CVE:** CVE-2024-10442
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation DS1823xs+
- **Credit:** Jack Dates of RET2 Systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-208/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology DiskStation DS1823xs+ devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of command data in the libsynobtrfsreplicacore.so.7 module. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_22

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated

# ZDI-25-1040: (Pwn2Own) Synology DiskStation DS925+ samlAuth Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1040
- **ZDI-CAN:** ZDI-CAN-28409
- **Date:** 2025-12-03
- **CVE:** CVE-2025-13392
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation DS925+
- **Credit:** Le Trong Phuc (chanze@VRC) and Cao Ngoc Quy (Chino Kafuu)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1040/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Synology DiskStation DS925+ devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SYNOPAMSSO::samlAuth method. The issue results from permitting authentication via a mechanism that should be disabled. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_25_14

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2025-12-03 - Coordinated public release of advisory
- 2025-12-03 - Advisory Updated

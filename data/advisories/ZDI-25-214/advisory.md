# ZDI-25-214: (Pwn2Own) Synology DiskStation DS1823xs+ Vue.JS Improper Neutralization of Argument Delimiters Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-214
- **ZDI-CAN:** ZDI-CAN-25403
- **Date:** 2025-04-09
- **CVE:** CVE-2024-10441
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation DS1823xs+
- **Credit:** Ryan Emmons (Rapid7)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-214/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology DiskStation DS1823xs+ devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the provided username during login. The issue results from the lack of proper validation of a user-supplied string before using it to construct environment variables. An attacker can leverage this vulnerability to execute code in the context of the root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_20

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated

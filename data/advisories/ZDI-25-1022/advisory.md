# ZDI-25-1022: Deciso OPNsense diag_backup.php filename Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1022
- **ZDI-CAN:** ZDI-CAN-28133
- **Date:** 2025-11-25
- **CVE:** CVE-2025-13698
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Deciso
- **Affected Products:** OPNsense
- **Credit:** Alex Williams from Pellera Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1022/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Deciso OPNsense. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of backup configuration files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Deciso has issued an update to correct this vulnerability. More details can be found at: https://github.com/opnsense/core/commit/cb15c935137d05c86a1e6cf12af877e9c32a23af

## Disclosure Timeline

- 2025-10-29 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2026-02-24 - Advisory Updated

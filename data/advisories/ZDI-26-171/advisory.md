# ZDI-26-171: Unraid Update Request Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-171
- **ZDI-CAN:** ZDI-CAN-28951
- **Date:** 2026-03-09
- **CVE:** CVE-2026-3838
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Unraid
- **Affected Products:** Unraid
- **Credit:** Nicolas Chatelain (Nicocha30)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Unraid. Authentication is required to exploit this vulnerability. The specific flaw exists within the update.php file. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in version 7.2.4.

## Disclosure Timeline

- 2026-02-19 - Vulnerability reported to vendor
- 2026-03-09 - Coordinated public release of advisory
- 2026-03-09 - Advisory Updated

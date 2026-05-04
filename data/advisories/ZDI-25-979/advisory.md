# ZDI-25-979: Netgate pfSense CE Suricata Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-979
- **ZDI-CAN:** ZDI-CAN-28085
- **Date:** 2025-10-30
- **CVE:** CVE-2025-12490
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Netgate
- **Affected Products:** pfSense
- **Credit:** Alex Williams from Pellera Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-979/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Netgate pfSense. Authentication is required to exploit this vulnerability. The specific flaw exists within the Suricata package. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of root.

## Additional Details

Netgate has issued an update to correct this vulnerability. More details can be found at: https://github.com/pfsense/FreeBSD-ports/commit/36b2303dfca35a1183d76f26bcc6ce26d4ea682d

## Disclosure Timeline

- 2025-10-15 - Vulnerability reported to vendor
- 2025-10-30 - Coordinated public release of advisory
- 2025-10-30 - Advisory Updated

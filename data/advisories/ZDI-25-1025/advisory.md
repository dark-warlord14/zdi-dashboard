# ZDI-25-1025: MariaDB mariadb-dump Utility Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1025
- **ZDI-CAN:** ZDI-CAN-27000
- **Date:** 2025-11-27
- **CVE:** CVE-2025-13699
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** MariaDB
- **Affected Products:** MariaDB
- **Credit:** Litezeraw
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MariaDB. Interaction with the mariadb-dump utility is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the handling of view names. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

MariaDB has issued an update to correct this vulnerability. More details can be found at: https://jira.mariadb.org/browse/MDEV-37483

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2025-11-27 - Coordinated public release of advisory
- 2025-11-27 - Advisory Updated

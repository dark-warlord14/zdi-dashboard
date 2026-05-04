# ZDI-25-951: Allegra DatabaseBackupBL Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-951
- **ZDI-CAN:** ZDI-CAN-27136
- **Date:** 2025-10-08
- **CVE:** CVE-2025-11466
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** Swagat
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-951/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Allegra. Authentication is required to exploit this vulnerability. The specific flaw exists within the DatabaseBackupBL class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://alltena.com/en/resources/release-notes/release-notes-for-release-8-1-6

## Disclosure Timeline

- 2025-07-08 - Vulnerability reported to vendor
- 2025-10-08 - Coordinated public release of advisory
- 2025-10-08 - Advisory Updated

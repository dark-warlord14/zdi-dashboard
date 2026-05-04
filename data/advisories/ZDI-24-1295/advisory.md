# ZDI-24-1295: Logsign Unified SecOps Platform delete_gsuite_key_file Input Validation Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1295
- **ZDI-CAN:** ZDI-CAN-25265
- **Date:** 2024-09-26
- **CVE:** CVE-2024-9257
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Abdessamad Lahlali and Smile Thanapattheerakul of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1295/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files within sensitive directories on affected installations of Logsign Unified SecOps Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the delete_gsuite_key_file endpoint. The issue results from the lack of proper validation of a user-supplied filename prior to using it in file operations. An attacker can leverage this vulnerability to delete critical files on the system.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/21062889743762-30-08-2024-Version-6-4-26-Release-Notes

## Disclosure Timeline

- 2024-08-27 - Vulnerability reported to vendor
- 2024-09-26 - Coordinated public release of advisory
- 2024-09-26 - Advisory Updated

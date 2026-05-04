# ZDI-24-1021: Logsign Unified SecOps Platform Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1021
- **ZDI-CAN:** ZDI-CAN-24680
- **Date:** 2024-07-30
- **CVE:** CVE-2024-7564
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Abdessamad Lahlali and Smile Thanapattheerakul of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1021/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Logsign Unified SecOps Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the get_response_json_result endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/20138814468754-14-07-2024-Version-6-4-13-Release-Notes

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

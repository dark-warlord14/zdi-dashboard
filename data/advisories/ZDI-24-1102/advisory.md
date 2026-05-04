# ZDI-24-1102: Logsign Unified SecOps Platform Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1102
- **ZDI-CAN:** ZDI-CAN-25027
- **Date:** 2024-08-08
- **CVE:** CVE-2024-7602
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Abdessamad Lahlali and Smile Thanapattheerakul of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1102/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Logsign Unified SecOps Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the HTTP API service, which listens on TCP port 443 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/20617133769362-06-08-2024-Version-6-4-23-Release-Notes

## Disclosure Timeline

- 2024-08-06 - Vulnerability reported to vendor
- 2024-08-08 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

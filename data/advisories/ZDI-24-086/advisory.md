# ZDI-24-086: TP-Link Omada ER605 Access Control Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-086
- **ZDI-CAN:** ZDI-CAN-22227
- **Date:** 2024-02-05
- **CVE:** CVE-2024-1180
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Omada ER605
- **Credit:** Noam Moshe of Claroty Research - Team82
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-086/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Omada ER605. Authentication is required to exploit this vulnerability. The specific issue exists within the handling of the name field in the access control user interface. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware: ER605(UN)_V2_2.2.3 Build 20231201

## Disclosure Timeline

- 2023-11-16 - Vulnerability reported to vendor
- 2024-02-05 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

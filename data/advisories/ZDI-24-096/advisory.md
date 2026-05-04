# ZDI-24-096: Oracle Product Lifecycle Management ExportServlet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-096
- **ZDI-CAN:** ZDI-CAN-21848
- **Date:** 2024-02-06
- **CVE:** CVE-2024-20953
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Product Lifecycle Management
- **Credit:** nexteam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Product Lifecycle Management. Authentication is required to exploit this vulnerability. The specific flaw exists within the ExportServlet. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2024.html

## Disclosure Timeline

- 2023-10-06 - Vulnerability reported to vendor
- 2024-02-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

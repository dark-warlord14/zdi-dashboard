# ZDI-24-072: Synology RT6600ax Qualcomm LDB Service Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-072
- **ZDI-CAN:** ZDI-CAN-19708
- **Date:** 2024-01-15
- **CVE:** CVE-2024-21473
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** RT6600ax
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-072/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology RT6600ax routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Qualcomm LDB service. The issue results from the lack of proper validation of user-supplied data prior to further processing. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Qualcomm fixed the issue in a customer-only security update on January 1st, 2024.

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2024-01-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

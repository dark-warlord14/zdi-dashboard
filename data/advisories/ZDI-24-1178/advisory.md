# ZDI-24-1178: Qualcomm Wi-Fi SON LDB Service Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1178
- **ZDI-CAN:** ZDI-CAN-24083
- **Date:** 2024-08-23
- **CVE:** CVE-2024-21473
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Qualcomm Technologies
- **Affected Products:** Wi-Fi SON
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1178/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of multiple Qualcomm chipsets. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Qualcomm LDB service. The issue results from the lack of proper validation of user-supplied data prior to further processing. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Qualcomm Technologies has issued an update to correct this vulnerability. More details can be found at: https://docs.qualcomm.com/product/publicresources/securitybulletin/april-2024-bulletin.html

## Disclosure Timeline

- 2024-04-30 - Vulnerability reported to vendor
- 2024-08-23 - Coordinated public release of advisory
- 2024-08-23 - Advisory Updated

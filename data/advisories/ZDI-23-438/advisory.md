# ZDI-23-438: ManageEngine ADManager Plus ChangePasswordAction Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-438
- **ZDI-CAN:** ZDI-CAN-20033
- **Date:** 2023-04-12
- **CVE:** CVE-2023-29084
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ADManager Plus
- **Credit:** Simon Humbert of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-438/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ManageEngine ADManager Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the ChangePasswordAction function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/ad-manager/admanager-kb/cve-2023-29084.html

## Disclosure Timeline

- 2023-01-12 - Vulnerability reported to vendor
- 2023-04-12 - Coordinated public release of advisory

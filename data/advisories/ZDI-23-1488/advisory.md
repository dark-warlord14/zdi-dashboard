# ZDI-23-1488: ManageEngine ADManager Plus installServiceWithCredentials Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1488
- **ZDI-CAN:** ZDI-CAN-21010
- **Date:** 2023-09-29
- **CVE:** CVE-2023-38743
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ADManager Plus
- **Credit:** Nguyen Quoc Viet (Petrus Viet) of VNG Security Researcher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1488/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ManageEngine ADManager Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the installServiceWithCredentials function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/ad-manager/admanager-kb/cve-2023-38743.html

## Disclosure Timeline

- 2023-06-07 - Vulnerability reported to vendor
- 2023-09-29 - Coordinated public release of advisory

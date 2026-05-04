# ZDI-23-1719: ManageEngine Recovery Manager Plus getEscapedValue Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1719
- **ZDI-CAN:** ZDI-CAN-21173
- **Date:** 2023-11-22
- **CVE:** CVE-2023-48646
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** Recovery Manager Plus
- **Credit:** hir0ot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1719/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ManageEngine Recovery Manager Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the getEscapedValue method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/ad-recovery-manager/advisory/CVE-2023-48646.html

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-11-22 - Coordinated public release of advisory

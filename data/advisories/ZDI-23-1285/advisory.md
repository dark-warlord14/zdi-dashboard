# ZDI-23-1285: PaperCut NG External User Lookup Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1285
- **ZDI-CAN:** ZDI-CAN-21013
- **Date:** 2023-08-30
- **CVE:** CVE-2023-39469
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PaperCut NG. Authentication is required to exploit this vulnerability. The specific flaw exists within the External User Lookup functionality. The issue results from the lack of proper validation of a user-supplied string before using it to execute Java code. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/SecurityBulletinJuly2023/

## Disclosure Timeline

- 2023-06-07 - Vulnerability reported to vendor
- 2023-08-30 - Coordinated public release of advisory
- 2023-09-07 - Advisory Updated

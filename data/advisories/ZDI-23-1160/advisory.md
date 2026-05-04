# ZDI-23-1160: Parse Server transformUpdate Prototype Pollution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1160
- **ZDI-CAN:** ZDI-CAN-19904
- **Date:** 2023-08-22
- **CVE:** CVE-2023-36475
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parse
- **Affected Products:** Server
- **Credit:** hir0ot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Parse Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the transformUpdate function. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Parse has issued an update to correct this vulnerability. More details can be found at: https://github.com/parse-community/parse-server/security/advisories/GHSA-462x-c3jw-7vr6

## Disclosure Timeline

- 2023-02-17 - Vulnerability reported to vendor
- 2023-08-22 - Coordinated public release of advisory

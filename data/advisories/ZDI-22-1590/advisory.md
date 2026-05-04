# ZDI-22-1590: Parse Server transformUpdate Prototype Pollution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1590
- **ZDI-CAN:** ZDI-CAN-18358
- **Date:** 2022-11-15
- **CVE:** CVE-2022-39396
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parse
- **Affected Products:** Server
- **Credit:** Mikhail Shcherbakov (KTH), Cristian-Alexandru Staicu (CISPA) and Musard Balliu (KTH)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1590/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Parse Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the transformUpdate function. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Parse has issued an update to correct this vulnerability. More details can be found at: https://github.com/parse-community/parse-server/security/advisories/GHSA-prm5-8g2m-24gg

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2022-11-15 - Coordinated public release of advisory

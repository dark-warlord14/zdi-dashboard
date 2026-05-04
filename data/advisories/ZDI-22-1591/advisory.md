# ZDI-22-1591: Parse Server buildUpdatedObject Prototype Pollution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1591
- **ZDI-CAN:** ZDI-CAN-18750
- **Date:** 2022-11-15
- **CVE:** CVE-2022-41878
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parse
- **Affected Products:** Server
- **Credit:** Mikhail Shcherbakov, Cristian-Alexandru Staicu and Musard Balliu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1591/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Parse Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the buildUpdatedObject function. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Parse has issued an update to correct this vulnerability. More details can be found at: https://github.com/parse-community/parse-server/security/advisories/GHSA-xprv-wvh7-qqqx

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2022-11-15 - Coordinated public release of advisory

# ZDI-24-900: Parse Server literalizeRegexPart SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-900
- **ZDI-CAN:** ZDI-CAN-19105
- **Date:** 2024-07-16
- **CVE:** CVE-2024-27298
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:L
- **Affected Vendors:** Parse
- **Affected Products:** Server
- **Credit:** Mikhail Shcherbakov (https://twitter.com/yu5k3)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-900/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Parse Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the literalizeRegexPart function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Parse has issued an update to correct this vulnerability. More details can be found at: https://github.com/parse-community/parse-server/security/advisories/GHSA-6927-3vr9-fxf2

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2024-07-16 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

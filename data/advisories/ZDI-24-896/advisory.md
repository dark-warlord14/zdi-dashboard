# ZDI-24-896: Parse Server literalizeRegexPart SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-896
- **ZDI-CAN:** ZDI-CAN-23894
- **Date:** 2024-07-03
- **CVE:** CVE-2024-39309
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parse
- **Affected Products:** Server
- **Credit:** Smile Thanapattheerakul of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-896/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Parse Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the literalizeRegexPart function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Parse has issued an update to correct this vulnerability. More details can be found at: https://github.com/parse-community/parse-server/security/advisories/GHSA-c2hr-cqg6-8j6r

## Disclosure Timeline

- 2024-04-02 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

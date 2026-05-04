# ZDI-23-1650: Adobe RoboHelp Server resolveDistinguishedName LDAP Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1650
- **ZDI-CAN:** ZDI-CAN-21309
- **Date:** 2023-11-15
- **CVE:** CVE-2023-22272
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1650/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe RoboHelp Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the resolveDistinguishedName method. The issue results from the lack of proper validation of a user-supplied string before using it to construct LDAP queries. An attacker can leverage this vulnerability to disclose sensitive information in the context of the application, including partial information about stored credentials.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/robohelp-server/apsb23-53.html

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory

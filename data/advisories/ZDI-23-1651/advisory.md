# ZDI-23-1651: Adobe RoboHelp Server getRHSGroupsForRoles SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1651
- **ZDI-CAN:** ZDI-CAN-21308
- **Date:** 2023-11-15
- **CVE:** CVE-2023-22268
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1651/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe RoboHelp Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the getRHSGroupsForRoles method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/robohelp-server/apsb23-53.html

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory

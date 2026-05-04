# ZDI-15-170: ManageEngine Applications Manager DBUtil port SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-170
- **ZDI-CAN:** ZDI-CAN-2470
- **Date:** 2015-05-06
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** Applications Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-170/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine Applications Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DBUtil class. The issue lies in the failure to sanitize user-supplied input prior to executing a SQL statement. An attacker could leverage this vulnerability to execute code under the context of the database, which defaults to SYSTEM.

## Additional Details

Upgrade to version 11 build 11912 or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-19 - Vulnerability reported to vendor
- 2015-05-06 - Coordinated public release of advisory

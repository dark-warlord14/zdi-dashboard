# ZDI-14-271: AlienVault OSSIM ws_data SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-271
- **ZDI-CAN:** ZDI-CAN-2181
- **Date:** 2014-08-01
- **CVE:** CVE-2014-5159
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** AlienVault
- **Affected Products:** OSSIM
- **Credit:** grimmlin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-271/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault OSSIM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ossim-framework service. The issue lies in the handling of the ws_data parameter due to a failure to use parameterized queries when using user-supplied data as part of a SQL query. An attacker could leverage this vulnerability to execute SQL under the context of the database.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: http://forums.alienvault.com/discussion/2559/security-advisory-multiple-vulnerabilities

## Disclosure Timeline

- 2014-03-06 - Vulnerability reported to vendor
- 2014-08-01 - Coordinated public release of advisory

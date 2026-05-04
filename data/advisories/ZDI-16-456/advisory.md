# ZDI-16-456: Trend Micro Control Manager AdHocQuery_CustomProfiles SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-456
- **ZDI-CAN:** ZDI-CAN-3636
- **Date:** 2016-08-09
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** k0rpr1t_z0mb1e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-456/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within AdHocQuery_CustomProfiles.aspx. The issue lies in the failure to sanitize user-supplied input prior to executing a SQL statement. An attacker could leverage this vulnerability to execute code under the context of the database.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/solution/en-US/1114749.aspx

## Disclosure Timeline

- 2016-03-29 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory

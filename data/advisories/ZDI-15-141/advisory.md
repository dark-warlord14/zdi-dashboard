# ZDI-15-141: ManageEngine OpManager DataComparisionServlet query SQL Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-141
- **ZDI-CAN:** ZDI-CAN-2456
- **Date:** 2015-04-15
- **CVE:** CVE-2014-7868
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpManager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-141/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine OpManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DataComparisonServlet servlet. The issue lies in the ability to execute arbitrary SQL statements. An attacker could leverage this vulnerability to execute code under the context of the database, which defaults to SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://support.zoho.com/portal/manageengine/helpcenter/articles/sql-injection-vulnerability-fix

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory

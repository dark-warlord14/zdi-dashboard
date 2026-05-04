# ZDI-15-179: ManageEngine OpManager UpdateProbeUpgradeStatus probeName SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-179
- **ZDI-CAN:** ZDI-CAN-2460
- **Date:** 2015-05-07
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpManager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-179/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine OpManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UpdateProbeUpgradeStatus servlet. The issue lies in the failure to sanitize user-supplied input prior to executing a SQL statement. An attacker could leverage this vulnerability to execute code under the context of the database, which defaults to SYSTEM.

## Additional Details

Upgrade to version 11.5 build 11500 or higher, to address this vulnerability.

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-05-07 - Coordinated public release of advisory

# ZDI-13-093: Hewlett-Packard Managed Printing Administrator mdbBuildValueBasedSQL() Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-093
- **ZDI-CAN:** ZDI-CAN-1668
- **Date:** 2013-05-29
- **CVE:** CVE-2012-5219
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Managed Printing Administration
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Managed Printing Administration. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mdbBuildValueBasedSQL function inside the mdbObjectWrapper class. It is possible for a remote, unauthenticated user to inject arbitrary SQL commands in a GET request which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03737200

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory

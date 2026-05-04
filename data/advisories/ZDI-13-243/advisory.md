# ZDI-13-243: Hewlett-Packard Intelligent Management Center APM monitorId SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-243
- **ZDI-CAN:** ZDI-CAN-1664
- **Date:** 2013-10-16
- **CVE:** CVE-2013-4827
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-243/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the APM module's AppDataDaoImpl class. The monitorId parameter does not sufficiently sanitize input, allowing for SQL injection without authentication. An attacker could leverage this vulnerability to retrieve the usernames and passwords of configured devices.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03943547

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory

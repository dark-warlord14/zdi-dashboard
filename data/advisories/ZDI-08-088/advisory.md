# ZDI-08-088: Oracle E-Business Suite Business Intelligence SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-088
- **ZDI-CAN:** ZDI-CAN-160
- **Date:** 2008-12-16
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle
- **Affected Products:** Database Server
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-088/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL on vulnerable installations of Oracle E-Business Suite Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists in the APPS.ICXSUPWF.DisplayContacts package. The procedure fails to validate the contents of a WHERE clause containing user supplied input. This allows an attacker to execute arbitrary SQL statements in the context of the APPS user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2007.html

## Disclosure Timeline

- 2007-01-29 - Vulnerability reported to vendor
- 2008-12-16 - Coordinated public release of advisory

# ZDI-11-016: Oracle Real User Experience Insight rsynclogdird SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-016
- **ZDI-CAN:** ZDI-CAN-690
- **Date:** 2011-01-18
- **CVE:** CVE-2010-3594
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Real User Experience Insight
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-016/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL on vulnerable installations of Oracle Real User Experience Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists within a portion of the application which parses log files. Due to the component escaping characters improperly when inserting into a UTF-8 database, a user can inject a quote and provide arbitrary SQL statements.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory

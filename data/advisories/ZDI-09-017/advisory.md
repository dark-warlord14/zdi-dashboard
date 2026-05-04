# ZDI-09-017: Oracle Applications Server 10g Format String Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-017
- **ZDI-CAN:** ZDI-CAN-248
- **Date:** 2009-04-14
- **CVE:** CVE-2009-0993
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle
- **Affected Products:** Application Server
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Applications Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Oracle Process Manager and Notification (opmn) daemon which is an HTTP daemon listening on a TCP port above 6000. The daemon fails to properly handle format string tokens in the POST URI when logging to the file $ORACLE_HOME/opmn/logs/opmn.log. Exploitation of this issue can result in arbitrary code execution.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2009.html

## Disclosure Timeline

- 2007-11-07 - Vulnerability reported to vendor
- 2009-04-14 - Coordinated public release of advisory

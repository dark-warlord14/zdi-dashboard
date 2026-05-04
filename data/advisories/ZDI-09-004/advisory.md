# ZDI-09-004: Oracle TimesTen evtdump Remote Format String Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-004
- **ZDI-CAN:** ZDI-CAN-300
- **Date:** 2009-01-14
- **CVE:** CVE-2008-5440
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle
- **Affected Products:** TimesTen
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle TimesTen. User interaction is not required to exploit this vulnerability. The specific flaw exists in the evtdump CGI module, which is used to write to an internal log file. The parameter 'msg' does not properly sanitize format string tokens and can be exploited to execute arbitrary code.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujan2009.html

## Disclosure Timeline

- 2008-04-07 - Vulnerability reported to vendor
- 2009-01-14 - Coordinated public release of advisory

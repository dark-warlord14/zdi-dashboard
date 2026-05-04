# ZDI-16-033: Oracle Application Testing Suite Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-033
- **ZDI-CAN:** ZDI-CAN-3356
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0487
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Application Testing Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-033/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Oracle Application Testing Suite. The specific flaw exists within the ActionServlet servlet. The process method for this servlet will bypass authentication if the URI starts with a specific string. By providing that string, and a directory traversal that follows it, an attacker is able to reach any URI that would map to that servlet without authentication.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-08 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory

# ZDI-09-003: Oracle Secure Backup exec_qr() Command Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-003
- **ZDI-CAN:** ZDI-CAN-224
- **Date:** 2009-01-14
- **CVE:** CVE-2008-5448
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Secure Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the routine exec_qr() defined in the web script login.php. The user-supplied variable $rbtool is improperly sanitized and later passed through a call to popen(), this can result in remote pre-authentication command injection.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujan2009.html

## Disclosure Timeline

- 2007-07-13 - Vulnerability reported to vendor
- 2009-01-14 - Coordinated public release of advisory

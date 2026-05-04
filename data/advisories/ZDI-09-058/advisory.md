# ZDI-09-058: Oracle Secure Backup Administration Server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-058
- **ZDI-CAN:** ZDI-CAN-443
- **Date:** 2009-08-18
- **CVE:** CVE-2009-1977
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-058/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Oracle Secure Backup. User interaction is not required to exploit this vulnerability. The specific flaw exists in the logic used to authenticate a user to the administration server running on port 443. The script login.php does not properly sanitize the 'username' variable before using it in a database query. A specially crafted 'username' allows unauthorized attackers to log in with full administrative capabilities.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2009.html

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-08-18 - Coordinated public release of advisory

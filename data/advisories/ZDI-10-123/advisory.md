# ZDI-10-123: Oracle Secure Backup Administration Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-123
- **ZDI-CAN:** ZDI-CAN-626
- **Date:** 2010-07-13
- **CVE:** CVE-2010-0904
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-123/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Oracle Secure Backup. The specific flaw exists within the register globals emulation layer which allows attackers to specify values for arbitrary program variables. When specific parameters are specified via the URI it is possible for an attacker to bypass the authentication mechanism and reach functionality otherwise inaccessible without proper credentials. This can be leveraged by remote attackers to trigger what were post-auth vulnerabilities without valid credentials.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2010.html

## Disclosure Timeline

- 2009-10-28 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory

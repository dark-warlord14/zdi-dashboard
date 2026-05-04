# ZDI-10-118: Oracle Secure Backup Administration uname Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-118
- **ZDI-CAN:** ZDI-CAN-583
- **Date:** 2010-07-13
- **CVE:** CVE-2010-0904
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-118/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Oracle Secure Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of user input to the uname variable of the login.php script running on the administration page of Oracle Secure Backup. Do to the lack of proper shell metacharacter filtering it is possible to bypass the login check. Successful exploitation of this vulnerability allows the attacker to access sensitive information running on the administration server without proper credentials.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2010.html

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory

# ZDI-10-121: Oracle Secure Backup Administration selector Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-121
- **ZDI-CAN:** ZDI-CAN-616
- **Date:** 2010-07-13
- **CVE:** CVE-2010-0906
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-121/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary commands on vulnerable installations of Oracle Secure Backup. Authentication is required to exploit this vulnerability but may be bypassed. The specific flaw exists in the handling of the 'selector[0]' variable to the script index.php used in the administration server running on port 443. Due to improper filtering of user data a specially crafted request could lead to arbitrary commands being executed under the credentials of the service.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2010.html

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory

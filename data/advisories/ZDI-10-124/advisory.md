# ZDI-10-124: Oracle Secure Backup Web Interface Various Post-Auth Command Injection Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-124
- **ZDI-CAN:** ZDI-CAN-653
- **Date:** 2010-07-13
- **CVE:** CVE-2010-0907
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary commands on vulnerable installations of Oracle Secure Backup. Authentication is required to exploit these vulnerabilities. The specific flaws exist due to how the application passes CGI parameters to the internal obtool binary running on port 443. Due to improper filtering of user data a specially crafted request could lead to arbitrary commands being executed under the credentials of the service.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2010.html

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory

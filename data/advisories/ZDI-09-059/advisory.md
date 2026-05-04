# ZDI-09-059: Oracle Secure Backup Administration Server Multiple Command Injection Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-09-059
- **ZDI-CAN:** ZDI-CAN-442
- **Date:** 2009-08-18
- **CVE:** CVE-2009-1978
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-059/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary commands on vulnerable installations of Oracle Secure Backup. User interaction is not required to exploit this vulnerability but an attacker must be authenticated. The specific flaw exists in the handling of various variables to the script property_box.php used in the administration server running on port 443. Due to improper filtering of user data a specially crafted request could lead to arbitrary commands being executed under the credentials of the SYSTEM account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2009.html

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-08-18 - Coordinated public release of advisory

# ZDI-21-083: Oracle Database Procedure Improper Privilege Management Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-083
- **ZDI-CAN:** ZDI-CAN-12156
- **Date:** 2021-01-22
- **CVE:** CVE-2021-2054
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Database
- **Credit:** Emad Al-Mousa
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-083/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle Database. Authentication is required to exploit this vulnerability. The specific flaw exists within the execution of stored procedures. When executing stored procedures, the process does not properly check the caller's privileges. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from users with limited privileges.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2021.html

## Disclosure Timeline

- 2020-12-18 - Vulnerability reported to vendor
- 2021-01-22 - Coordinated public release of advisory

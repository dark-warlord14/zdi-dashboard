# ZDI-20-502: Oracle E-Business Suite Human Resources Organization Hierarchy Viewer OrgServer SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-502
- **ZDI-CAN:** ZDI-CAN-10465
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2882
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** E-Business Suite
- **Credit:** John Simpson of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-502/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Oracle E-Business Suite Human Resources. Authentication is required to exploit this vulnerability. The specific flaw exists within the Organization Hierarchy Viewer. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges and reset the password for the SYSADMIN user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-02-07 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory

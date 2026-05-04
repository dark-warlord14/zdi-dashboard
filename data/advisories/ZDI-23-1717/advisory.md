# ZDI-23-1717: NETGEAR ProSAFE Network Management System clearAlertByIds SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1717
- **ZDI-CAN:** ZDI-CAN-21875
- **Date:** 2023-11-20
- **CVE:** CVE-2023-44449
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Alex Williams of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1717/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of NETGEAR ProSAFE Network Management System. Authentication is required to exploit this vulnerability. The specific flaw exists within the clearAlertByIds function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065866/Security-Advisory-for-Multiple-Vulnerabilities-on-the-NMS300-PSV-2023-0114-PSV-2023-0115

## Disclosure Timeline

- 2023-08-10 - Vulnerability reported to vendor
- 2023-11-20 - Coordinated public release of advisory

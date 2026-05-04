# ZDI-24-902: NETGEAR ProSAFE Network Management System getSortString SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-902
- **ZDI-CAN:** ZDI-CAN-23207
- **Date:** 2024-07-18
- **CVE:** CVE-2024-6813
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-902/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Authentication is required to exploit this vulnerability. The specific flaw exists within the getSortString method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000066231/Security-Advisory-for-SQL-Injection-on-the-NMS300-PSV-2024-0018

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-07-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

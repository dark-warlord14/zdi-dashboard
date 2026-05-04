# ZDI-15-039: Persistent Systems Client Automation Remote Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-039
- **ZDI-CAN:** ZDI-CAN-1916
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1498
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Persistent Systems
- **Affected Products:** Radia Client Automation
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Persistent Systems Client Automation. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of certain requests (including getUsers, addAssigneesToRole, and removeAssigneesFromRole). Incomplete authentication allows for crafted packets to enumerate the users on the system and change the roles of users on the system without valid credentials. By using this, an attacker with access to any valid account on the system is able to execute arbitrary code on all clients controlled by the system.

## Additional Details

Persistent Systems has issued an update to correct this vulnerability. More details can be found at: https://radiasupport.accelerite.com/hc/en-us/articles/203659814-Accelerite-releases-solutions-and-best-practices-to-enhance-the-security-for-RBAC-and-Remote-Notify-features

## Disclosure Timeline

- 2014-04-16 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory

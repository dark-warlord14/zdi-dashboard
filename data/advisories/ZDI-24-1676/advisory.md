# ZDI-24-1676: ManageEngine Analytics Plus getOAToken Exposed Dangerous Method Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1676
- **ZDI-CAN:** ZDI-CAN-25135
- **Date:** 2024-12-11
- **CVE:** CVE-2024-52323
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** Analytics Plus
- **Credit:** Mohamed Mekkawy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1676/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of ManageEngine Analytics Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the getOAToken action. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/analytics-plus/CVE-2024-52323.html

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated

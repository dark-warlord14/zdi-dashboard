# ZDI-23-229: ManageEngine ServiceDesk Plus MSP generateSQLReport Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-229
- **ZDI-CAN:** ZDI-CAN-19536
- **Date:** 2023-03-09
- **CVE:** CVE-2023-26600
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ServiceDesk Plus MSP
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-229/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of ManageEngine ServiceDesk Plus MSP. Authentication is required to exploit this vulnerability. The specific flaw exists within the generateSQLReport function. The issue results from the lack of proper validation of user-supplied data. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/service-desk/CVE-2023-26600.html

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-03-09 - Coordinated public release of advisory

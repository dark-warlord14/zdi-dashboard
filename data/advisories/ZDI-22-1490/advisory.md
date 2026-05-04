# ZDI-22-1490: ManageEngine ServiceDesk Plus MSP exportMickeyList Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1490
- **ZDI-CAN:** ZDI-CAN-18608
- **Date:** 2022-11-15
- **CVE:** CVE-2022-40773
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ServiceDesk Plus MSP
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1490/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of ManageEngine ServiceDesk Plus MSP. Authentication is required to exploit this vulnerability. The specific flaw exists within the exportMickeyList action. The issue results from the lack of proper validation of user-supplied data. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/service-desk-msp/cve-2022-40773.html

## Disclosure Timeline

- 2022-09-08 - Vulnerability reported to vendor
- 2022-11-15 - Coordinated public release of advisory
- 2022-11-15 - Advisory Updated

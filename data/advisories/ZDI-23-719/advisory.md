# ZDI-23-719: D-Link D-View showUser Improper Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-719
- **ZDI-CAN:** ZDI-CAN-19534
- **Date:** 2023-05-24
- **CVE:** CVE-2023-32168
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-719/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of D-Link D-View. Authentication is required to exploit this vulnerability. The specific flaw exists within the showUser method. The issue results from the lack of proper authorization before accessing a privileged endpoint. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10332

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory

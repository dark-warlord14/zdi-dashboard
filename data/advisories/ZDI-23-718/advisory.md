# ZDI-23-718: D-Link D-View uploadMib Directory Traversal Arbitrary File Creation or Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-718
- **ZDI-CAN:** ZDI-CAN-19529
- **Date:** 2023-05-24
- **CVE:** CVE-2023-32167
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-718/
## Vulnerability Details

This vulnerability allows remote attackers to create and delete arbitrary files on affected installations of D-Link D-View. Authentication is required to exploit this vulnerability. The specific flaw exists within the uploadMib function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create or delete files in the context of SYSTEM.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10332

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory

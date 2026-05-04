# ZDI-23-715: D-Link D-View TftpSendFileThread Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-715
- **ZDI-CAN:** ZDI-CAN-19496
- **Date:** 2023-05-24
- **CVE:** CVE-2023-32164
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-715/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of D-Link D-View. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TftpSendFileThread class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10332

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory

# ZDI-21-976: D-Link DAP-2020 webproc getpage Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-976
- **ZDI-CAN:** ZDI-CAN-12103
- **Date:** 2021-08-18
- **CVE:** CVE-2021-34860
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2020
- **Credit:** chung96vn of Vietnam National Cyber Security Center
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-976/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of D-Link DAP-2020 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the getpage parameter provided to the webproc endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10201

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-08-18 - Coordinated public release of advisory

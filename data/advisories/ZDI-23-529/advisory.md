# ZDI-23-529: D-Link DAP-1360 webproc WEB_DisplayPage Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-529
- **ZDI-CAN:** ZDI-CAN-18415
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32137
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1360
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-529/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of D-Link DAP-1360 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of requests to the /cgi-bin/webproc endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10324

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

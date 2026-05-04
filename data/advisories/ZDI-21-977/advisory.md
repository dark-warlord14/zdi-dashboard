# ZDI-21-977: D-Link DAP-2020 webproc Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-977
- **ZDI-CAN:** ZDI-CAN-12104
- **Date:** 2021-08-18
- **CVE:** CVE-2021-34861
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2020
- **Credit:** chung96vn ft phieulang ft ChiTran
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-977/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-2020 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the webproc endpoint, which listens on TCP port 80 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10201

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-08-18 - Coordinated public release of advisory

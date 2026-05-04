# ZDI-22-1290: D-Link Multiple Routers lighttpd Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1290
- **ZDI-CAN:** ZDI-CAN-13796
- **Date:** 2022-09-20
- **CVE:** CVE-2022-41140
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** Multiple Routers
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1290/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of multiple D-Link routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the lighttpd service, which listens on TCP port 80 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10291

## Disclosure Timeline

- 2022-02-16 - Vulnerability reported to vendor
- 2022-09-20 - Coordinated public release of advisory

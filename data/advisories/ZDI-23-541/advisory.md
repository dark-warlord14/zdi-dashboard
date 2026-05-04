# ZDI-23-541: D-Link DIR-2640 prog.cgi Request Handling Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-541
- **ZDI-CAN:** ZDI-CAN-19546
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32149
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2640
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-541/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-2640 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web management interface, which listens on TCP port 80 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10323

## Disclosure Timeline

- 2022-12-22 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

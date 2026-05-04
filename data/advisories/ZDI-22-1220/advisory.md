# ZDI-22-1220: D-Link DIR-2150 anweb action_handler Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1220
- **ZDI-CAN:** ZDI-CAN-15727
- **Date:** 2022-09-14
- **CVE:** CVE-2022-40717
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2150
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1220/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected D-Link DIR-2150 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the anweb service, which listens on TCP ports 80 and 443 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10304

## Disclosure Timeline

- 2022-04-01 - Vulnerability reported to vendor
- 2022-09-14 - Coordinated public release of advisory

# ZDI-23-1815: D-Link G416 httpd Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1815
- **ZDI-CAN:** ZDI-CAN-21287
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50199
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** G416
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1815/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link G416 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP service listening on TCP port 80. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to gain access to critical functions on the device.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10367

## Disclosure Timeline

- 2023-07-14 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory

# ZDI-23-1828: D-Link G416 httpd Improper Handling of Exceptional Conditions Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1828
- **ZDI-CAN:** ZDI-CAN-21664
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50212
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** G416
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1828/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of D-Link G416 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP service listening on TCP port 80. The issue results from the lack of proper handling of error conditions. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10367

## Disclosure Timeline

- 2023-07-14 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory

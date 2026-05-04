# ZDI-20-1427: D-Link Multiple Routers dhttpd Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1427
- **ZDI-CAN:** ZDI-CAN-10912
- **Date:** 2020-12-15
- **CVE:** CVE-2020-27863
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** Multiple Routers
- **Credit:** chung96vn ft Hoang Le (phieulang)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1427/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of D-Link DVA-2800 and DSL-2888A routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dhttpd service, which listens on TCP port 8008 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10196

## Disclosure Timeline

- 2020-06-12 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
- 2021-09-27 - Advisory Updated

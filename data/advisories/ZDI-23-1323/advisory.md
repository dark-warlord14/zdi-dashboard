# ZDI-23-1323: D-Link DAP-1325 CGI Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1323
- **ZDI-CAN:** ZDI-CAN-18804
- **Date:** 2023-09-07
- **CVE:** CVE-2023-41186
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1325
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1323/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to access various functionality on affected installations of D-Link DAP-1325 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the CGI interface. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10351

## Disclosure Timeline

- 2022-09-28 - Vulnerability reported to vendor
- 2023-09-07 - Coordinated public release of advisory

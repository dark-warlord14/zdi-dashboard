# ZDI-23-1255: D-Link DAP-2622 DDP Get SSID List WPA PSK Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1255
- **ZDI-CAN:** ZDI-CAN-20078
- **Date:** 2023-08-25
- **CVE:** CVE-2023-35750
- **CVSS:** 7.4
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2622
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1255/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of D-Link DAP-2622 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DDP service. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10349

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-08-25 - Coordinated public release of advisory

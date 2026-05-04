# ZDI-23-1230: D-Link DAP-2622 Telnet CLI Use of Hardcoded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1230
- **ZDI-CAN:** ZDI-CAN-20050
- **Date:** 2023-08-25
- **CVE:** CVE-2023-35724
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2622
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1230/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DAP-2622 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CLI service, which listens on TCP port 23. The server program contains hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10349

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-08-25 - Coordinated public release of advisory

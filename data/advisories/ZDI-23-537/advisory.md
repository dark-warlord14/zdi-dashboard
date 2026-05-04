# ZDI-23-537: D-Link DAP-1360 Hardcoded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-537
- **ZDI-CAN:** ZDI-CAN-18455
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32145
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1360
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-537/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DAP-1360 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of login requests to the web-based user interface. The firmware contains hard-coded default credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10324

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

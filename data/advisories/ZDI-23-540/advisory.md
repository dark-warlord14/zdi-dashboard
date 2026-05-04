# ZDI-23-540: D-Link DIR-2640 HNAP PrivateLogin Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-540
- **ZDI-CAN:** ZDI-CAN-19545
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32148
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2640
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-540/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-2640 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web management interface, which listens on TCP port 80 by default. A crafted XML element in the login request can cause authentication to succeed without providing proper credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10323

## Disclosure Timeline

- 2022-12-21 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

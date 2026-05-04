# ZDI-22-1222: D-Link DIR-2150 xupnpd ui_upload Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1222
- **ZDI-CAN:** ZDI-CAN-15905
- **Date:** 2022-09-14
- **CVE:** CVE-2022-3210
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2150
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1222/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary commands on affected installations of D-Link DIR-2150 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the xupnpd service, which listens on TCP port 4044 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10304

## Disclosure Timeline

- 2022-04-13 - Vulnerability reported to vendor
- 2022-09-14 - Coordinated public release of advisory

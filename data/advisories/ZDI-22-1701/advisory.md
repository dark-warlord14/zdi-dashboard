# ZDI-22-1701: D-Link DIR-825/EE xupnpd YouTube Plugin Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1701
- **ZDI-CAN:** ZDI-CAN-19222
- **Date:** 2022-12-28
- **CVE:** CVE-2022-43642
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-825
- **Credit:** Pap Gergo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1701/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-825/EE routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the YouTube plugin for the xupnpd service, which listens on TCP port 4044. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the admin user.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10319

## Disclosure Timeline

- 2022-11-23 - Vulnerability reported to vendor
- 2022-12-28 - Coordinated public release of advisory

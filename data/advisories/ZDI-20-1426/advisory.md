# ZDI-20-1426: D-Link Multiple Routers dhttpd Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1426
- **ZDI-CAN:** ZDI-CAN-10911
- **Date:** 2020-12-15
- **CVE:** CVE-2020-27862
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** Multiple Routers
- **Credit:** chung96vn ft Hoang Le (phieulang)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1426/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DVA-2800 and DSL-2888A routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dhttpd service, which listens on TCP port 8008 by default. When parsing the path parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the web server.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10196

## Disclosure Timeline

- 2020-06-12 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
- 2021-09-27 - Advisory Updated

# ZDI-23-535: D-Link DAP-1360 webupg UPGCGI_CheckAuth Numeric Truncation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-535
- **ZDI-CAN:** ZDI-CAN-18423
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32143
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1360
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-535/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1360 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of requests to the /cgi-bin/webupg endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10324

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

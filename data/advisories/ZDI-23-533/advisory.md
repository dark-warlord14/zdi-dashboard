# ZDI-23-533: D-Link DAP-1360 webproc WEB_DisplayPage Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-533
- **ZDI-CAN:** ZDI-CAN-18419
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32141
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1360
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-533/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1360 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of requests to the /cgi-bin/webproc endpoint. When parsing the getpage and errorpage parameters, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10324

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

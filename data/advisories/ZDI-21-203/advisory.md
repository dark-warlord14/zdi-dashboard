# ZDI-21-203: D-Link DAP-2020 webproc getpage Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-203
- **ZDI-CAN:** ZDI-CAN-10932
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27248
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2020
- **Credit:** chung96vn ft Hoang Le (phieulang)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-203/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-2020 Wi-Fi access points. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of CGI scripts. When parsing the getpage parameter, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10201

## Disclosure Timeline

- 2020-08-21 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2021-09-27 - Advisory Updated

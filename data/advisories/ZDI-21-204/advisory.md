# ZDI-21-204: D-Link DAP-2020 WEB_CmdFileList Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-204
- **ZDI-CAN:** ZDI-CAN-11369
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27249
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2020
- **Credit:** Anthony Schneiter & Jannis Kirschner from Team SUID (in alphabetical order)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-204/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-2020 Wi-Fi access points. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of CGI scripts. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10201

## Disclosure Timeline

- 2020-09-08 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory

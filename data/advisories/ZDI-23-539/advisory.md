# ZDI-23-539: D-Link DIR-2640 LocalIPAddress Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-539
- **ZDI-CAN:** ZDI-CAN-19544
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32147
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2640
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-539/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-2640 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the LocalIPAddress parameter provided to the HNAP1 endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10323

## Disclosure Timeline

- 2022-12-21 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

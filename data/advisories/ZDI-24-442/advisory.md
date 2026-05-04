# ZDI-24-442: (0Day) D-Link DIR-2150 GetDeviceSettings Target Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-442
- **ZDI-CAN:** ZDI-CAN-21235
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5291
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2150
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-442/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-2150 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SOAP API interface, which listens on TCP port 80 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

07/12/23 – ZDI reported the vulnerability to the vendor 11/09/23 – ZDI asked for updates 11/21/23 –The vendor communicated that the case was not fixed 12/12/23 – ZDI asked for updates 12/26/23 –The vendor communicated that the case was not fixed and a failed patch announcement was published https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10336 5/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: On May 14, 2024, the vendor informed ZDI about the beta software update v1.06beta Hotfix https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10376

## Disclosure Timeline

- 2023-07-12 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

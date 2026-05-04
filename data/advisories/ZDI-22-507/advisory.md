# ZDI-22-507: Cisco Nexus Dashboard Fabric Controller Improper Privilege Management Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-507
- **ZDI-CAN:** ZDI-CAN-14806
- **Date:** 2022-03-11
- **CVE:** CVE-2017-5641
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Nexus Dashboard Fabric Controller
- **Credit:** Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-507/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Cisco Nexus Dashboard Fabric Controller. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of a user permission. A crafted tcpdump command can trigger execution of a privileged operation. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Fixed in version 11.5(4) or later

## Disclosure Timeline

- 2021-09-10 - Vulnerability reported to vendor
- 2022-03-11 - Coordinated public release of advisory

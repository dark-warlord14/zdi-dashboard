# ZDI-24-409: Oracle VirtualBox Guest Additions Improper Access Control Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-409
- **ZDI-CAN:** ZDI-CAN-23388
- **Date:** 2024-04-26
- **CVE:** CVE-2024-21110
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-409/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. In addition, some user interaction is required on the part of a user on the host. The specific flaw exists within Guest Additions. The issue results from improper access control when performing upgrade operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root on the target guest system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-15 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

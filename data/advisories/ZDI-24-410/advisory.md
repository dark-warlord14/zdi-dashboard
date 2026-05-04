# ZDI-24-410: Oracle VirtualBox vboxdrv Improper Privilege Management Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-410
- **ZDI-CAN:** ZDI-CAN-23403
- **Date:** 2024-04-26
- **CVE:** CVE-2024-21116
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-410/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the vboxdrv kernel module. The issue results from improper privilege management. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

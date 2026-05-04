# ZDI-22-1442: Oracle VirtualBox COM RPC Interface Improper Access Control Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1442
- **ZDI-CAN:** ZDI-CAN-17589
- **Date:** 2022-10-21
- **CVE:** CVE-2022-39427
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Exist(@exist91240480)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1442/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the COM RPC Interface. The issue results from improper access control. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2022.html

## Disclosure Timeline

- 2022-07-22 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory

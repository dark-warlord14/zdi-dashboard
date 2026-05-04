# ZDI-24-413: (Pwn2Own) Oracle VirtualBox DevVGA Out-Of-Bounds Write Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-413
- **ZDI-CAN:** ZDI-CAN-23796
- **Date:** 2024-04-26
- **CVE:** CVE-2024-21115
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Cody Gallagher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-413/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the DevVGA module. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

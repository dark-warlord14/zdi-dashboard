# ZDI-24-776: (Pwn2Own) Oracle VirtualBox OHCI USB Controller Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-776
- **ZDI-CAN:** ZDI-CAN-23777
- **Date:** 2024-06-14
- **CVE:** CVE-2024-21121
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** ColdEye
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-776/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the virtual OHCI USB controller. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-06-14 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

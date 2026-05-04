# ZDI-21-937: (Pwn2Own) Parallels Desktop Toolgate Uncontrolled Memory Allocation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-937
- **ZDI-CAN:** ZDI-CAN-13544
- **Date:** 2021-08-03
- **CVE:** CVE-2021-34854
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Billy Jheng Bing-Jhong (@st424204), Calvin Fong (@__lord_idiot) & Muhammad Alifa Ramdhan (@n0psledbyte) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-937/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of user-supplied data, which can result in an uncontrolled memory allocation. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2021-08-03 - Coordinated public release of advisory

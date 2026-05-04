# ZDI-21-938: (Pwn2Own) Parallels Desktop virtio-gpu Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-938
- **ZDI-CAN:** ZDI-CAN-13581
- **Date:** 2021-08-03
- **CVE:** CVE-2021-34856
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ben McBride
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-938/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the virtio-gpu virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2021-08-03 - Coordinated public release of advisory

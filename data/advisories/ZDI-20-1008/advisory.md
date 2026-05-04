# ZDI-20-1008: Parallels Desktop hypervisor Out-Of-Bounds Read Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1008
- **ZDI-CAN:** ZDI-CAN-10030
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17390
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** grigoritchy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1008/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the hypervisor kernel extension. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-03-15 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory

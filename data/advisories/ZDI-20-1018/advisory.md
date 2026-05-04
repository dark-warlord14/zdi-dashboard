# ZDI-20-1018: Parallels Desktop prl_hypervisor Out-Of-Bounds Read Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1018
- **ZDI-CAN:** ZDI-CAN-11304
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17400
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** grigoritchy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1018/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the prl_hypervisor kext. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory

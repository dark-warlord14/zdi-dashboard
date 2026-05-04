# ZDI-20-298: VMware Workstation vmnetdhcp Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-298
- **ZDI-CAN:** ZDI-CAN-9292
- **Date:** 2020-03-13
- **CVE:** CVE-2020-3947
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-298/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the vmnetdhcp.exe module. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0004.html

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-03-13 - Coordinated public release of advisory

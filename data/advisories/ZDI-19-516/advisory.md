# ZDI-19-516: VMware Workstation e1000 Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-516
- **ZDI-CAN:** ZDI-CAN-7804
- **Date:** 2019-05-29
- **CVE:** CVE-2019-5515
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** instructor
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-516/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the e1000 driver. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2019-0005.html

## Disclosure Timeline

- 2019-04-02 - Vulnerability reported to vendor
- 2019-05-29 - Coordinated public release of advisory

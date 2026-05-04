# ZDI-19-988: VMware Workstation e1000 Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-988
- **ZDI-CAN:** ZDI-CAN-8933
- **Date:** 2019-11-13
- **CVE:** CVE-2019-5541
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** instructor
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-988/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of virtualized e1000 devices. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2019-0021.html

## Disclosure Timeline

- 2019-09-17 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory

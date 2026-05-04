# ZDI-20-781: VMware Workstation xHCI Isoch TD Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-781
- **ZDI-CAN:** ZDI-CAN-10097
- **Date:** 2020-06-30
- **CVE:** CVE-2020-3968
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-781/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the xHCI component. When parsing Isoch Transfer Descriptor (TD), the process does not properly validate user-supplied data that can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0015.html

## Disclosure Timeline

- 2020-02-04 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated

# ZDI-22-003: VMware Workstation SCSI Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-003
- **ZDI-CAN:** ZDI-CAN-14237
- **Date:** 2022-01-06
- **CVE:** CVE-2021-22045
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Jaanus Kääp, Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-003/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the SCSI component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2022-0001.html

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
- 2022-01-11 - Advisory Updated

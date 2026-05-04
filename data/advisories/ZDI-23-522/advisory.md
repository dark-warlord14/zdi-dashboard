# ZDI-23-522: (Pwn2Own) VMware Workstation UHCI Component Stack-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-522
- **ZDI-CAN:** ZDI-CAN-20773
- **Date:** 2023-05-01
- **CVE:** CVE-2023-20869
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Nguyễn Hoàng Thạch (@hi_im_d4rkn3ss) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-522/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the UHCI component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0008.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory

# ZDI-23-521: (Pwn2Own) VMware Workstation UHCI Component Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-521
- **ZDI-CAN:** ZDI-CAN-20719
- **Date:** 2023-05-01
- **CVE:** CVE-2023-20870
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Nguyễn Hoàng Thạch (@hi_im_d4rkn3ss) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-521/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the UHCI component. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0008.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory

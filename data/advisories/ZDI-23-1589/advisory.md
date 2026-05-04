# ZDI-23-1589: VMware Workstation UHCI Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1589
- **ZDI-CAN:** ZDI-CAN-21512
- **Date:** 2023-11-06
- **CVE:** CVE-2023-34044
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Gwangun Jung (@pr0Ln) at THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1589/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the UHCI component. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0022.html

## Disclosure Timeline

- 2023-07-27 - Vulnerability reported to vendor
- 2023-11-06 - Coordinated public release of advisory

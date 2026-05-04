# ZDI-20-1268: VMware Workstation BDOOR_CMD_PATCH_ACPI_TABLES Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1268
- **ZDI-CAN:** ZDI-CAN-11228
- **Date:** 2020-10-20
- **CVE:** CVE-2020-3982
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1268/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the BDOOR_CMD_PATCH_ACPI_TABLES command. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0023.html

## Disclosure Timeline

- 2020-06-18 - Vulnerability reported to vendor
- 2020-10-20 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated

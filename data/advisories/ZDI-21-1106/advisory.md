# ZDI-21-1106: VMware vCenter Server Appliance Service Lifecycle Manager Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1106
- **ZDI-CAN:** ZDI-CAN-13426
- **Date:** 2021-09-22
- **CVE:** CVE-2021-22015
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** vCenter Server Appliance
- **Credit:** Sergey Gerasimov of Solidlab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1106/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware vCenter Server Appliance. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Service Lifecycle Manager. The issue results from incorrect permissions set on a shell script. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0020.html

## Disclosure Timeline

- 2021-05-18 - Vulnerability reported to vendor
- 2021-09-22 - Coordinated public release of advisory

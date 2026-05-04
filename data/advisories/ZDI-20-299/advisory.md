# ZDI-20-299: VMware Workstation Virtual Printer External Control of File Name Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-299
- **ZDI-CAN:** ZDI-CAN-10099
- **Date:** 2020-03-13
- **CVE:** CVE-2020-3948
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-299/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Virtual Printer module. The issue results from the lack of proper validation of a user-supplied shared object file path prior to loading the file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0004.html

## Disclosure Timeline

- 2020-01-17 - Vulnerability reported to vendor
- 2020-03-13 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated

# ZDI-20-1177: VMware Workstation ThinPrint name Table Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1177
- **ZDI-CAN:** ZDI-CAN-10922
- **Date:** 2020-09-15
- **CVE:** CVE-2020-3989
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** linhlhq of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1177/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the ThinPrint component. Crafted data in the name table of a font file can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0020.html

## Disclosure Timeline

- 2020-04-30 - Vulnerability reported to vendor
- 2020-09-15 - Coordinated public release of advisory

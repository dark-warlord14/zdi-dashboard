# ZDI-19-421: (Pwn2Own) VMware Workstation UHCI Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-421
- **ZDI-CAN:** ZDI-CAN-8372
- **Date:** 2019-04-17
- **CVE:** CVE-2019-5518
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-421/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of data sent to UHCI endpoints. Crafted data sent to UHCI endpoints can trigger a memory access past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2019-0005.html

## Disclosure Timeline

- 2019-03-21 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated

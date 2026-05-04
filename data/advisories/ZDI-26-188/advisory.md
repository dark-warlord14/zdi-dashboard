# ZDI-26-188: (Pwn2Own) VMware ESXi VMCI Integer Underflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-188
- **ZDI-CAN:** ZDI-CAN-27176
- **Date:** 2026-03-16
- **CVE:** CVE-2025-41237
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Corentin "@OnlyTheDuck" BAYET from REverse Tactics
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-188/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware ESXi. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of VMCI. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877

## Disclosure Timeline

- 2025-05-23 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

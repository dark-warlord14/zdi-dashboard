# ZDI-26-190: (Pwn2Own) VMware Workstation PVSCSI Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-190
- **ZDI-CAN:** ZDI-CAN-27175
- **Date:** 2026-03-16
- **CVE:** CVE-2025-41238
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Thomas Bouzerar (@MajorTomSec) from @Synacktiv, Etienne Helluy-Lafont from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-190/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the PVSCSI virtual device. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877

## Disclosure Timeline

- 2025-05-23 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

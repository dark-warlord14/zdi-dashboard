# ZDI-25-729: (Pwn2Own) Canonical Ubuntu Kernel taprio Scheduler Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-729
- **ZDI-CAN:** ZDI-CAN-23656
- **Date:** 2025-07-30
- **CVE:** CVE-2024-50126
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Kyle Zeng from ASU SEFCOM
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-729/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the taprio scheduler. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/CVE-2024-50126

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2025-07-30 - Coordinated public release of advisory
- 2025-07-30 - Advisory Updated

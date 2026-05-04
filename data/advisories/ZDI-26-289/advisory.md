# ZDI-26-289: Linux Kernel ETS Scheduler Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-289
- **ZDI-CAN:** ZDI-CAN-28490
- **Date:** 2026-04-15
- **CVE:** CVE-2025-71066
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Maher Azzouzi (@maherazz2)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-289/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Qdisc objects. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/netdev/20251128151919.576920-1-jhs@mojatatu.com/T/

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated

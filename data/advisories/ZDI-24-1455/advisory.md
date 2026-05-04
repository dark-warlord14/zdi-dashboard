# ZDI-24-1455: Linux Kernel Net Scheduler ATM Queuing Discipline Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1455
- **ZDI-CAN:** ZDI-CAN-23237
- **Date:** 2024-11-05
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Pumpkin (@u1f383) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1455/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of traffic control. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=v6.1.113&id=09038f47e45cd5dbb02315db2134403a6b160ceb

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-11-05 - Coordinated public release of advisory
- 2024-11-05 - Advisory Updated

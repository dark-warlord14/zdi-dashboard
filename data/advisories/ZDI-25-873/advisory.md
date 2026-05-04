# ZDI-25-873: Linux Kernel perf Subsystem AUX Buffers Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-873
- **ZDI-CAN:** ZDI-CAN-27504
- **Date:** 2025-08-28
- **CVE:** CVE-2025-38563
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-873/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of reference counters. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b024d7b56c77191cde544f838debb7f8451cd0d6

## Disclosure Timeline

- 2025-07-29 - Vulnerability reported to vendor
- 2025-08-28 - Coordinated public release of advisory
- 2025-09-24 - Advisory Updated

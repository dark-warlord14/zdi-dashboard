# ZDI-25-915: Linux Kernel io_uring Futex Request Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-915
- **ZDI-CAN:** ZDI-CAN-27561
- **Date:** 2025-09-24
- **CVE:** CVE-2025-39698
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** ReDress
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-915/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the the io_uring subsystem. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/io_uring/futex.c?id=508c1314b342b78591f51c4b5dadee31a88335df

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2025-09-24 - Coordinated public release of advisory
- 2025-09-24 - Advisory Updated

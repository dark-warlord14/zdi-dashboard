# ZDI-22-362: Linux Kernel io_uring Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-362
- **ZDI-CAN:** ZDI-CAN-14621
- **Date:** 2022-02-16
- **CVE:** CVE-2022-1043
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-362/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of credentials in io_uring. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/a30f895ad3239f45012e860d4f94c1a388b36d14

## Disclosure Timeline

- 2021-08-20 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
- 2022-07-21 - Advisory Updated

# ZDI-21-001: Linux Kernel io_uring Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-001
- **ZDI-CAN:** ZDI-CAN-11480
- **Date:** 2021-01-04
- **CVE:** CVE-2021-20226
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-001/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of file descriptors in io_uring. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Fixed in version 5.10.2

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-01-04 - Coordinated public release of advisory

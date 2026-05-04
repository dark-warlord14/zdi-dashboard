# ZDI-21-100: Linux Kernel setsockopt System Call Untrusted Pointer Dereference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-100
- **ZDI-CAN:** ZDI-CAN-11171
- **Date:** 2021-01-29
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-100/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of arguments to the setsockopt system call. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Fixed in Kernel v5.4.92

## Disclosure Timeline

- 2020-12-22 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory

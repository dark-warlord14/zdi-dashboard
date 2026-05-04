# ZDI-21-1148: Linux Kernel eBPF Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1148
- **ZDI-CAN:** ZDI-CAN-14689
- **Date:** 2021-10-13
- **CVE:** CVE-2021-34866
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1148/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs, which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in version 5.13.14

## Disclosure Timeline

- 2021-08-20 - Vulnerability reported to vendor
- 2021-10-13 - Coordinated public release of advisory

# ZDI-23-1489: Linux Kernel eBPF Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1489
- **ZDI-CAN:** ZDI-CAN-19399
- **Date:** 2023-09-29
- **CVE:** CVE-2023-39191
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1489/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs prior to executing them. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20230121002241.2113993-1-memxor@gmail.com/

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-09-29 - Coordinated public release of advisory

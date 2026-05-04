# ZDI-21-101: Linux Kernel eBPF Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-101
- **ZDI-CAN:** ZDI-CAN-12547
- **Date:** 2021-01-29
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** De4dCr0w
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-101/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs prior to executing them. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Fixed in Kernel 5.10.10

## Disclosure Timeline

- 2021-01-15 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory

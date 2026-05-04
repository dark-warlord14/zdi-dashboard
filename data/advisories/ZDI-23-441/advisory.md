# ZDI-23-441: Linux Kernel udmabuf Improper Validation of Array Index Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-441
- **ZDI-CAN:** ZDI-CAN-17639
- **Date:** 2023-04-13
- **CVE:** CVE-2023-2008
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Manuel Blanco Parajón; Eloi Sanfelix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-441/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within a fault handler. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/05b252cccb2e5c3f56119d25de684b4f810ba4

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2023-04-13 - Coordinated public release of advisory

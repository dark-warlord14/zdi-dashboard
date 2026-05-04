# ZDI-24-593: Linux Kernel Net Scheduler Out-Of-Bounds Access Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-593
- **ZDI-CAN:** ZDI-CAN-18568
- **Date:** 2024-06-10
- **CVE:** CVE-2023-31436
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Gwangun Jung at THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-593/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the MTU value provided to the QFQ Scheduler. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=2192671

## Disclosure Timeline

- 2022-09-14 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

# ZDI-26-250: Linux Kernel Analog Device Driver Improper Validation of Array Index Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-250
- **ZDI-CAN:** ZDI-CAN-28893
- **Date:** 2026-03-31
- **CVE:** CVE-2026-23092
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-250/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of debugfs commands. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=978d28136c53df38f8f0b747191930e2f95e9084

## Disclosure Timeline

- 2026-01-13 - Vulnerability reported to vendor
- 2026-03-31 - Coordinated public release of advisory
- 2026-03-31 - Advisory Updated

# ZDI-22-961: Linux Kernel LightNVM Subsystem Heap-based Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-961
- **ZDI-CAN:** ZDI-CAN-17325
- **Date:** 2022-07-11
- **CVE:** N/A
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-961/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the LightNVM subsystem. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/drivers/lightnvm/Kconfig?h=v5.10.114&id=549209caabc89f2877ad5f62d11fca5c052e0e8

## Disclosure Timeline

- 2022-04-27 - Vulnerability reported to vendor
- 2022-07-11 - Coordinated public release of advisory

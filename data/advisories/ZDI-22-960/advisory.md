# ZDI-22-960: Linux Kernel LightNVM Subsystem Heap-based Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-960
- **ZDI-CAN:** ZDI-CAN-17194
- **Date:** 2022-07-11
- **CVE:** CVE-2022-2991
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-960/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the LightNVM subsystem. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/drivers/lightnvm/Kconfig?h=v5.10.114&id=549209caabc89f2877ad5f62d11fca5c052e0e8 https://access.redhat.com/security/cve/CVE-2022-2991

## Disclosure Timeline

- 2022-04-27 - Vulnerability reported to vendor
- 2022-07-11 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated

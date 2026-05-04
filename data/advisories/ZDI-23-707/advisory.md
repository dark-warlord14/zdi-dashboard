# ZDI-23-707: Linux Kernel vmwgfx Driver Race Condition Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-707
- **ZDI-CAN:** ZDI-CAN-20110
- **Date:** 2023-05-17
- **CVE:** CVE-2023-33951
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-707/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of GEM objects. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to disclose information in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/drivers/gpu/drm/vmwgfx/vmwgfx_bo.c?h=v6.4-rc1&id=9ef8d83e8e25d5f1811b3a38eb1484f85f64296c

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2023-05-26 - Advisory Updated

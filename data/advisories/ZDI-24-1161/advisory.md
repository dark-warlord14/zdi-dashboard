# ZDI-24-1161: Linux Kernel vmwgfx Driver Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1161
- **ZDI-CAN:** ZDI-CAN-23566
- **Date:** 2024-08-22
- **CVE:** CVE-2024-36960
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Berk Cem Goksel of SAFA Team, Kuzey Arda Bulut
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1161/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of vmw fence events. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/a37ef7613c00f2d72c8fc08bd83fb6cc76926c8c

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated

# ZDI-24-195: Linux Kernel ksmbd TCP Connection Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-195
- **ZDI-CAN:** ZDI-CAN-22991
- **Date:** 2024-02-23
- **CVE:** CVE-2024-26592
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** fffvr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-195/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of TCP connection and disconnection. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/38d20c62903d669693a1869aa68c4dd5674e2544

## Disclosure Timeline

- 2024-01-11 - Vulnerability reported to vendor
- 2024-02-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

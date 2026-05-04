# ZDI-24-1456: Linux Kernel ksmbd Session Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1456
- **ZDI-CAN:** ZDI-CAN-25282
- **Date:** 2024-11-05
- **CVE:** N/A
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** fffvr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1456/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the implementation of session setup and logoff. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git/commit/?id=498c77d275c70b6084d5b8ce5284ae8d2d06f065

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2024-11-05 - Coordinated public release of advisory
- 2024-11-05 - Advisory Updated

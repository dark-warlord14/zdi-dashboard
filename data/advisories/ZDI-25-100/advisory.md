# ZDI-25-100: Linux Kernel ksmbd Session Setup Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-100
- **ZDI-CAN:** ZDI-CAN-25737
- **Date:** 2025-02-27
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Hexrabbit (@h3xr4bb1t) of DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the implementation of session setup. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git/commit/?id=0a1483d5bf25bcd0974db5ac284d575be6f4e47f

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-02-27 - Coordinated public release of advisory
- 2025-02-27 - Advisory Updated

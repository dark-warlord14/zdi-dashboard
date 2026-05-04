# ZDI-24-996: Linux Kernel ksmbd ACL Inheritance Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-996
- **ZDI-CAN:** ZDI-CAN-22271
- **Date:** 2024-07-29
- **CVE:** CVE-2023-52755
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-996/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication may or may not be required to exploit this vulnerability, depending upon configuration. Furthermore, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of ACL attributes. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20231124172008.838629931@linuxfoundation.org/

## Disclosure Timeline

- 2023-11-03 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

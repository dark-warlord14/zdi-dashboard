# ZDI-24-227: Linux Kernel ksmbd Chained Request Improper Input Validation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-227
- **ZDI-CAN:** ZDI-CAN-21506
- **Date:** 2024-03-01
- **CVE:** CVE-2023-52442
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-227/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of chained requests. The issue results from the lack of proper validation of user-supplied requests prior to processing them. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/3df0411e132ee74a87aa13142dfd2b190275332e

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2024-03-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

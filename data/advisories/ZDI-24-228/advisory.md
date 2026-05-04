# ZDI-24-228: Linux Kernel ksmbd Negotiate Request Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-228
- **ZDI-CAN:** ZDI-CAN-21541
- **Date:** 2024-03-01
- **CVE:** CVE-2023-52441
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-228/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of SMB2 negotiate requests. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/536bb492d39bb6c080c92f31e8a55fe9934f452b

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2024-03-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

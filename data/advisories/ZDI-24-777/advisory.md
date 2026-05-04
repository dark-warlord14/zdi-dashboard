# ZDI-24-777: Linux Kernel ksmbd Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-777
- **ZDI-CAN:** ZDI-CAN-21826
- **Date:** 2024-06-14
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-777/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication may or may not be required to exploit this vulnerability, depending upon configuration. Furthermore, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the parsing of SMB2 requests. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in Linux 6.5-rc7 https://github.com/torvalds/linux/commit/5aa4fda5aa9c2a5a7bac67b4a12b089ab81fee3c

## Disclosure Timeline

- 2023-08-22 - Vulnerability reported to vendor
- 2024-06-14 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

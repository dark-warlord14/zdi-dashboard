# ZDI-24-194: Linux Kernel ksmbd Mech Token Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-194
- **ZDI-CAN:** ZDI-CAN-22890
- **Date:** 2024-02-23
- **CVE:** CVE-2024-26594
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** fffvr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-194/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of SMB2 Mech Tokens. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/92e470163d96df8db6c4fa0f484e4a229edb903d

## Disclosure Timeline

- 2024-01-11 - Vulnerability reported to vendor
- 2024-02-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

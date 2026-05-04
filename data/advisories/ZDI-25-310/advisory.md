# ZDI-25-310: Linux Kernel ksmbd Session Setup Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-310
- **ZDI-CAN:** ZDI-CAN-26505
- **Date:** 2025-05-29
- **CVE:** CVE-2025-22037
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Viacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-310/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of preauth hashes. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/c8b5b7c5da7d0c31c9b7190b4a7bba5281fc4780

## Disclosure Timeline

- 2025-03-25 - Vulnerability reported to vendor
- 2025-05-29 - Coordinated public release of advisory
- 2025-06-03 - Advisory Updated

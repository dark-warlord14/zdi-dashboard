# ZDI-25-917: Linux Kernel ksmbd generate_key context.iov_base Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-917
- **ZDI-CAN:** ZDI-CAN-27654
- **Date:** 2025-09-24
- **CVE:** CVE-2025-38562
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-917/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of the Linux Kernel. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of a context value when updating a hash function. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.16.1

## Disclosure Timeline

- 2025-07-18 - Vulnerability reported to vendor
- 2025-09-24 - Coordinated public release of advisory
- 2025-09-24 - Advisory Updated

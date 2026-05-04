# ZDI-25-610: Linux Kernel ksmbd destroy_previous_session Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-610
- **ZDI-CAN:** ZDI-CAN-27391
- **Date:** 2025-07-17
- **CVE:** CVE-2025-38191
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-610/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of the Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the destroy_previous_session function. The issue results from the lack of proper validation of a pointer prior to accessing it. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=7ac5b66acafcc9292fb935d7e03790f2b8b2dc0e

## Disclosure Timeline

- 2025-06-12 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated

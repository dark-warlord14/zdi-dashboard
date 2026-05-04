# ZDI-23-979: Linux Kernel ksmbd Chained Request NULL Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-979
- **ZDI-CAN:** ZDI-CAN-21165
- **Date:** 2023-07-28
- **CVE:** CVE-2023-3866
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** 8437438cb38d8565e9a990474a7b8d2b3e3770a521eb159325e93c6189f526d1
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-979/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of chained requests. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20230626180806.105257976@linuxfoundation.org/

## Disclosure Timeline

- 2023-06-13 - Vulnerability reported to vendor
- 2023-07-28 - Coordinated public release of advisory
- 2024-04-17 - Advisory Updated

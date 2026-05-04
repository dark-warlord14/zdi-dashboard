# ZDI-24-589: Linux Kernel ksmbd Read Request Memory Leak Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-589
- **ZDI-CAN:** ZDI-CAN-21588
- **Date:** 2024-06-10
- **CVE:** CVE-2023-39180
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-589/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of SMB2_READ commands. The issue results from not releasing memory after its effective lifetime. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/lkml/20230813160006.1073695-11-sashal@kernel.org/

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

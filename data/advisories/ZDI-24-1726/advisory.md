# ZDI-24-1726: Linux Kernel ksmbd TCP Connection Memory Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1726
- **ZDI-CAN:** ZDI-CAN-25738
- **Date:** 2024-12-20
- **CVE:** CVE-2024-50285
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t) of DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1726/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of the Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of new TCP connections. The issue results from the lack of memory release after its effective lifetime. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/linux-cve-announce/2024111946-CVE-2024-50285-6013@gregkh/

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2024-12-20 - Coordinated public release of advisory
- 2024-12-20 - Advisory Updated

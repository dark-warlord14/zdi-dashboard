# ZDI-22-1687: Linux Kernel ksmbd Memory Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1687
- **ZDI-CAN:** ZDI-CAN-17815
- **Date:** 2022-12-22
- **CVE:** CVE-2022-47941
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1687/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SMB2_NEGOTIATE commands. The issue results from the lack of memory release after its effective lifetime. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.61

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2022-12-22 - Coordinated public release of advisory
- 2023-01-23 - Advisory Updated

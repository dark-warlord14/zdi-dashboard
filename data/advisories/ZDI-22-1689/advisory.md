# ZDI-22-1689: Linux Kernel ksmbd Out-Of-Bounds Read Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1689
- **ZDI-CAN:** ZDI-CAN-17818
- **Date:** 2022-12-22
- **CVE:** CVE-2022-47938
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1689/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of SMB2_TREE_CONNECT commands. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.61

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2022-12-22 - Coordinated public release of advisory
- 2023-01-23 - Advisory Updated

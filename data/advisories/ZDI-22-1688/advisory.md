# ZDI-22-1688: Linux Kernel ksmbd Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1688
- **ZDI-CAN:** ZDI-CAN-17771
- **Date:** 2022-12-22
- **CVE:** CVE-2022-47942
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1688/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of file attributes. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/lkml/20220819153711.847846093@linuxfoundation.org/

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2022-12-22 - Coordinated public release of advisory
- 2023-01-23 - Advisory Updated

# ZDI-23-693: Linux Kernel ksmbd Memory Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-693
- **ZDI-CAN:** ZDI-CAN-18259
- **Date:** 2023-05-17
- **CVE:** CVE-2023-2593
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-693/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of the Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of new TCP connections. The issue results from the lack of memory release after its effective lifetime. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/lkml/CAH2r5msyEy20e=FBx6wPWWc3kXzNR4b+zHshSqidRdFKVf_7Jg@mail.gmail.com/

## Disclosure Timeline

- 2022-08-19 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

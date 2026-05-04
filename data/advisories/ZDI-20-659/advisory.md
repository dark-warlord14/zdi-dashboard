# ZDI-20-659: FreeBSD Kernel NAT Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-659
- **ZDI-CAN:** ZDI-CAN-10624
- **Date:** 2020-05-19
- **CVE:** CVE-2020-7454
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** FreeBSD
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-659/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of FreeBSD Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of NAT. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of kernel.

## Additional Details

FreeBSD has issued an update to correct this vulnerability. More details can be found at: https://www.freebsd.org/security/advisories/FreeBSD-SA-20:12.libalias.asc

## Disclosure Timeline

- 2020-03-15 - Vulnerability reported to vendor
- 2020-05-19 - Coordinated public release of advisory

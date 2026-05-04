# ZDI-22-806: FreeBSD 802.11 Network Subsystem Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-806
- **ZDI-CAN:** ZDI-CAN-15980
- **Date:** 2022-05-31
- **CVE:** CVE-2022-23088
- **CVSS:** 8.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** FreeBSD
- **Affected Products:** Kernel
- **Credit:** m00nbsd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-806/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of FreeBSD Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of 802.11 Wi-Fi beacon frames. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

FreeBSD has issued an update to correct this vulnerability. More details can be found at: https://www.freebsd.org/security/advisories/FreeBSD-SA-22:07.wifi_meshid.asc

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-05-31 - Coordinated public release of advisory

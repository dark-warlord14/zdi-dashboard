# ZDI-22-1405: Linux Kernel IPv4 FIB Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1405
- **ZDI-CAN:** ZDI-CAN-18902
- **Date:** 2022-10-07
- **CVE:** N/A
- **CVSS:** 2.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Gwangun Jung (@pr0Ln) at THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1405/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the fib_create_info function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/netdev/20221005181257.8897-1-dsahern@kernel.org/T/#u

## Disclosure Timeline

- 2022-10-04 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory

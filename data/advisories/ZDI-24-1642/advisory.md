# ZDI-24-1642: Linux Kernel nftables Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1642
- **ZDI-CAN:** ZDI-CAN-24348
- **Date:** 2024-12-03
- **CVE:** CVE-2024-42070
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t) of DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1642/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of packet filtering. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/linux-cve-announce/2024072952-CVE-2024-42070-b271@gregkh/

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-12-03 - Coordinated public release of advisory
- 2024-12-03 - Advisory Updated

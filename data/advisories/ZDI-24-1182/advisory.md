# ZDI-24-1182: Linux Kernel Netfilter Conntrack Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1182
- **ZDI-CAN:** ZDI-CAN-24591
- **Date:** 2024-08-27
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1182/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of connection tracking. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://patchwork.kernel.org/project/netdevbpf/patch/20240717215214.225394-2-pablo@netfilter.org/

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-08-27 - Coordinated public release of advisory
- 2024-08-27 - Advisory Updated

# ZDI-23-899: (Pwn2Own) Linux Kernel nftables Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-899
- **ZDI-CAN:** ZDI-CAN-20717
- **Date:** 2023-07-06
- **CVE:** CVE-2023-31248
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Mingi Cho of Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-899/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of nft_chains. The issue results from the lack of validating the status of a chain while processing lookup on the chain. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/netfilter-devel/20230705121627.GC19489@breakpoint.cc/T/

## Disclosure Timeline

- 2023-05-09 - Vulnerability reported to vendor
- 2023-07-06 - Coordinated public release of advisory

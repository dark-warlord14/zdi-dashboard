# ZDI-23-900: (Pwn2Own) Linux Kernel nftables Incorrect Pointer Scaling Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-900
- **ZDI-CAN:** ZDI-CAN-20721
- **Date:** 2023-07-06
- **CVE:** CVE-2023-35001
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Tanguy DUBROCA (@SidewayRE) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-900/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of nft chains. The issue results from incorrect pointer scaling, which can result in a memory access past the end of an array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/netfilter-devel/20230705121515.747251-1-cascardo@canonical.com/T/

## Disclosure Timeline

- 2023-05-09 - Vulnerability reported to vendor
- 2023-07-06 - Coordinated public release of advisory

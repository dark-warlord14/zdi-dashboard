# ZDI-23-702: Linux Kernel ksmbd Tree Connection Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-702
- **ZDI-CAN:** ZDI-CAN-20592
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32254
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-702/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of SMB2_TREE_DISCONNECT commands. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/30210947a343b6b3ca13adc9bfc88e1543e16dd5

## Disclosure Timeline

- 2023-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

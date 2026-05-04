# ZDI-23-696: Linux Kernel ksmbd Tree Connection NULL Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-696
- **ZDI-CAN:** ZDI-CAN-20479
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32248
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-696/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of SMB2_TREE_CONNECT and SMB2_QUERY_INFO commands. The issue results from the lack of proper validation of a pointer prior to accessing it. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/3ac00a2ab69b34189942afa9e862d5170cdcb018

## Disclosure Timeline

- 2023-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

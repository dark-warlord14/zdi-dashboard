# ZDI-23-698: Linux Kernel ksmbd Session Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-698
- **ZDI-CAN:** ZDI-CAN-20481
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32250
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-698/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of SMB2_SESSION_SETUP commands. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/f5c779b7ddbda30866cf2a27c63e34158f858c73

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

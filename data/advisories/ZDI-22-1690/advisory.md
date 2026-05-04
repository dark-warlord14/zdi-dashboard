# ZDI-22-1690: Linux Kernel ksmbd Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1690
- **ZDI-CAN:** ZDI-CAN-17816
- **Date:** 2022-12-22
- **CVE:** CVE-2022-47939
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1690/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of SMB2_TREE_DISCONNECT commands. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.61

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2022-12-22 - Coordinated public release of advisory
- 2023-01-23 - Advisory Updated

# ZDI-23-703: Linux Kernel ksmbd Session Setup Memory Leak Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-703
- **ZDI-CAN:** ZDI-CAN-20593
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32255
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-703/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of SMB2_SESSION_SETUP commands. The issue results from the lack of memory release after its effective lifetime. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/6d7cb549c2ca20e1f07593f15e936fd54b763028

## Disclosure Timeline

- 2023-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

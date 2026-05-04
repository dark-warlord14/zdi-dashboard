# ZDI-23-699: Linux Kernel ksmbd Improper Restriction of Excessive Authentication Attempts Protection Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-699
- **ZDI-CAN:** ZDI-CAN-20482
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32251
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-699/
## Vulnerability Details

This vulnerability allows remote attackers to create a brute force condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of asynchronous connections. The issue results from the lack of protection of an authentication mechanism. An attacker can leverage this vulnerability to brute force the credentials on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/b096d97f47326b1e2dbdef1c91fab69ffda54d17

## Disclosure Timeline

- 2023-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

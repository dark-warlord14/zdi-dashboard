# ZDI-23-697: Linux Kernel ksmbd Multichannel Improper Authentication Session Hijack Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-697
- **ZDI-CAN:** ZDI-CAN-20480
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32249
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-697/
## Vulnerability Details

This vulnerability allows remote attackers to hijack a session on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of Session ID within Multichannel. The issue results from the lack of proper isolation when performing lookup on a session. An attacker can leverage this vulnerability to hijack arbitrary live session on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/3353ab2df5f68dab7da8d5ebb427a2d265a1f2b2

## Disclosure Timeline

- 2023-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory

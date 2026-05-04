# ZDI-24-1647: BlueZ Classic HID Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1647
- **ZDI-CAN:** ZDI-CAN-25398
- **Date:** 2024-12-10
- **CVE:** CVE-2024-8805
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** BlueZ
- **Affected Products:** BlueZ
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1647/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of BlueZ. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of Classic HID connections. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

https://patchwork.kernel.org/project/bluetooth/patch/20240912204458.3037144-1-luiz.dentz@gmail.com/ https://git.kernel.org/pub/scm/linux/kernel/git/bluetooth/bluetooth-next.git/commit/?id=370e38c32529e0899bb387a70d5d92dfb5a2b3c5

## Disclosure Timeline

- 2024-10-15 - Vulnerability reported to vendor
- 2024-12-10 - Coordinated public release of advisory
- 2024-12-10 - Advisory Updated

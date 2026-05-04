# ZDI-22-263: (Pwn2Own) TP-Link AC1750 NetUSB Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-263
- **ZDI-CAN:** ZDI-CAN-15769
- **Date:** 2022-02-10
- **CVE:** CVE-2022-24353
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** AC1750
- **Credit:** Bien Pham (@bienpnn) from Team Orca of Sea Security (security.sea.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-263/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetUSB.ko module. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the root user.

## Additional Details

Fixed in firmware 211210

## Disclosure Timeline

- 2021-11-08 - Vulnerability reported to vendor
- 2022-02-10 - Coordinated public release of advisory

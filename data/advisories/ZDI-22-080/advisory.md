# ZDI-22-080: TP-Link Archer C90 DNS Response Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-080
- **ZDI-CAN:** ZDI-CAN-14655
- **Date:** 2022-01-17
- **CVE:** CVE-2021-35003
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer C90
- **Credit:** Team FLASHBACK: Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) + Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TP-Link Archer C90 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DNS responses. A crafted DNS message can trigger an overflow of a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in version 6

## Disclosure Timeline

- 2021-09-16 - Vulnerability reported to vendor
- 2022-01-17 - Coordinated public release of advisory

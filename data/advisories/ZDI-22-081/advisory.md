# ZDI-22-081: TP-Link TL-WA1201 DNS Response Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-081
- **ZDI-CAN:** ZDI-CAN-14656
- **Date:** 2022-01-17
- **CVE:** CVE-2021-35004
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WA1201
- **Credit:** Team FLASHBACK: Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) + Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-081/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TP-Link TL-WA1201 wireless access points. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DNS responses. A crafted DNS message can trigger an overflow of a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in version 2

## Disclosure Timeline

- 2021-09-16 - Vulnerability reported to vendor
- 2022-01-17 - Coordinated public release of advisory

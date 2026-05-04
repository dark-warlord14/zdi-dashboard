# ZDI-21-214: TP-Link Archer A7 Protection Mechanism Failure Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-214
- **ZDI-CAN:** ZDI-CAN-12309
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27245
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** Team FLASHBACK: Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) + Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-214/
## Vulnerability Details

This vulnerability allows a firewall bypass on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of IPv6 connections. The issue results from the lack of proper filtering of IPv6 SSH connections. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Fixed in V5

## Disclosure Timeline

- 2020-11-06 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2021-03-19 - Advisory Updated

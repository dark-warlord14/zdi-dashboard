# ZDI-20-338: (Pwn2Own) TP-Link Archer A7 Protection Mechanism Failure Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-338
- **ZDI-CAN:** ZDI-CAN-9663
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10887
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** F-Secure Labs - Mark Barnes, Toby Drew, Max Van Amerongen, and James Loureiro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-338/
## Vulnerability Details

This vulnerability allows a firewall bypass on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of IPv6 connections. The issue results from the lack of proper filtering of IPv6 SSH connections. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory

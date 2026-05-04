# ZDI-21-215: TP-Link AC1750 sync-server Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-215
- **ZDI-CAN:** ZDI-CAN-12306
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27246
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** AC1750
- **Credit:** @0xMitsurugi (Synacktiv), @swapgs (Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-215/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of MAC addresses by the tdpServer endpoint. A crafted TCP message can write stack pointers to the stack. An attacker can leverage this vulnerability to execute code in the context of the root user.

## Additional Details

Fixed in V5

## Disclosure Timeline

- 2020-11-06 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2021-03-19 - Advisory Updated

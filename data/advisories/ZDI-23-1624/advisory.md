# ZDI-23-1624: TP-Link TL-WR841N ated_tp Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1624
- **ZDI-CAN:** ZDI-CAN-21825
- **Date:** 2023-11-14
- **CVE:** CVE-2023-39471
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR841N
- **Credit:** Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1624/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link TL-WR841N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ated_tp service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware: TL-WR841N(US)_V14_231119: https://www.tp-link.com/us/support/download/tl-wr841n/v14/#Firmware TL-WR840N(KR)_V6.20_231121: https://www.tp-link.com/kr/support/download/tl-wr840n/#Firmware

## Disclosure Timeline

- 2023-08-29 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
- 2023-12-05 - Advisory Updated

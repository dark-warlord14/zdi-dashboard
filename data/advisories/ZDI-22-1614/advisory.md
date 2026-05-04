# ZDI-22-1614: TP-Link TL-WR940N httpd Use of Insufficiently Random Values Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1614
- **ZDI-CAN:** ZDI-CAN-18334
- **Date:** 2022-11-21
- **CVE:** CVE-2022-43636
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR940N
- **Credit:** ExLuck
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1614/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of TP-Link TL-WR940N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from the lack of sufficient randomness in the sequnce numbers used for session managment. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in TL-WR940N(US)_V6_3.20.1 Build 220801

## Disclosure Timeline

- 2022-08-25 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
- 2023-03-28 - Advisory Updated

# ZDI-22-1615: TP-Link TL-WR940N httpd Incorrect Implementation of Authentication Algorithm Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1615
- **ZDI-CAN:** ZDI-CAN-17332
- **Date:** 2022-11-21
- **CVE:** CVE-2022-43635
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR940N
- **Credit:** ExLuck
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1615/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of TP-Link TL-WR940N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from the incorrect implementation of the authentication algorithm. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in TL-WR940N(US)_V6_3.20.1 Build 220801

## Disclosure Timeline

- 2022-08-25 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory

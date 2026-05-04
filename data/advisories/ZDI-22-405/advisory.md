# ZDI-22-405: TP-Link TL-WR940N httpd Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-405
- **ZDI-CAN:** ZDI-CAN-13911
- **Date:** 2022-02-22
- **CVE:** CVE-2022-24972
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR940N
- **Credit:** Vadym Kolisnichenko
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-405/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of TP-Link TL-WR940N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from the lack of proper access control. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in firmware 211111

## Disclosure Timeline

- 2021-10-21 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory

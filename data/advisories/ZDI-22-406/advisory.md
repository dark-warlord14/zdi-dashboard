# ZDI-22-406: TP-Link TL-WR940N httpd ssid1 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-406
- **ZDI-CAN:** ZDI-CAN-13992
- **Date:** 2022-02-22
- **CVE:** CVE-2022-24973
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR940N
- **Credit:** Vadym Kolisnichenko
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-406/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link TL-WR940N routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware 211111

## Disclosure Timeline

- 2021-10-21 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory

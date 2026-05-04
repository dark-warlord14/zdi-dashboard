# ZDI-22-265: TP-Link TL-WR940N httpd httpRpmFs Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-265
- **ZDI-CAN:** ZDI-CAN-13910
- **Date:** 2022-02-10
- **CVE:** CVE-2022-24355
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR940N
- **Credit:** Vadym Kolisnichenko
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-265/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link TL-WR940N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of file name extensions. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware 211111

## Disclosure Timeline

- 2021-10-21 - Vulnerability reported to vendor
- 2022-02-10 - Coordinated public release of advisory

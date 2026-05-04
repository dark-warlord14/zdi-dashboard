# ZDI-23-377: TP-Link AX1800 Firmware Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-377
- **ZDI-CAN:** ZDI-CAN-19703
- **Date:** 2023-03-31
- **CVE:** CVE-2023-27346
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** AX1800
- **Credit:** Kevin Wang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-377/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link AX1800 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of firmware images. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in AX21 version V3230219 https://www.tp-link.com/us/support/download/archer-ax21/v3/#Firmware

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory

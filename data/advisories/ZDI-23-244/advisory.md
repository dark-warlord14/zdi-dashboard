# ZDI-23-244: TP-Link Archer AX21 tmpServer Command 0x422 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-244
- **ZDI-CAN:** ZDI-CAN-19905
- **Date:** 2023-03-15
- **CVE:** CVE-2023-27333
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer AX21
- **Credit:** Pumpkin, working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-244/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Archer AX21 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of command 0x422 provided to the tmpServer service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in Archer AX21 version V3230219 https://www.tp-link.com/us/support/download/archer-ax21/#Firmware

## Disclosure Timeline

- 2023-01-26 - Vulnerability reported to vendor
- 2023-03-15 - Coordinated public release of advisory

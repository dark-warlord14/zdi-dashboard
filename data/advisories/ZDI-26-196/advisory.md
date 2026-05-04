# ZDI-26-196: (Pwn2Own) ChargePoint Home Flex OCPP getpreq Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-196
- **ZDI-CAN:** ZDI-CAN-26339
- **Date:** 2026-03-16
- **CVE:** CVE-2026-4156
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ChargePoint
- **Affected Products:** Home Flex
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-196/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of ChargePoint Home Flex EV chargers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OCPP messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in CPH50 firmware version 5.5.4.22

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

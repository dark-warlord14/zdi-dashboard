# ZDI-26-197: (Pwn2Own) ChargePoint Home Flex revssh Service Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-197
- **ZDI-CAN:** ZDI-CAN-26338
- **Date:** 2026-03-16
- **CVE:** CVE-2026-4157
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ChargePoint
- **Affected Products:** Home Flex
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-197/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of ChargePoint Home Flex devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OCPP messages. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in CPH50 firmware version 5.5.4.22

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated

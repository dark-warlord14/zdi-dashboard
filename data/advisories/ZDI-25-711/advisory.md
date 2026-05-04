# ZDI-25-711: (Pwn2Own) Tesla Wall Connector Content-Length Header Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-711
- **ZDI-CAN:** ZDI-CAN-26300
- **Date:** 2025-07-29
- **CVE:** CVE-2025-8320
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Wall Connector
- **Credit:** PHP Hooligans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-711/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Tesla Wall Connector devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of the HTTP Content-Length header. The issue results from the lack of proper validation of user-supplied data, which can result in memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in Firmware Version 24.44.3

## Disclosure Timeline

- 2025-03-12 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated

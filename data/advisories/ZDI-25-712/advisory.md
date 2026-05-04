# ZDI-25-712: (Pwn2Own) Tesla Wall Connector Firmware Downgrade Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-712
- **ZDI-CAN:** ZDI-CAN-26299
- **Date:** 2025-07-29
- **CVE:** CVE-2025-8321
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Wall Connector
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-712/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Tesla Wall Connector devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware upgrade feature. The issue results from the lack of an anti-downgrade mechanism. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the device.

## Additional Details

Fixed in Firmware Version 24.44.3

## Disclosure Timeline

- 2025-03-14 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated

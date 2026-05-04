# ZDI-25-261: (Pwn2Own) Tesla Model S oFono AT Command Heap-based Buffer Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-261
- **ZDI-CAN:** ZDI-CAN-23198
- **Date:** 2025-04-30
- **CVE:** CVE-2024-6031
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model S
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-261/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected Tesla Model S vehicles. An attacker must first obtain the ability to execute code on the target modem in order to exploit this vulnerability. The specific flaw exists within the parsing of responses from AT commands. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in Firmware Version 2024.2

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated

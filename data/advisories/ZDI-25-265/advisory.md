# ZDI-25-265: (Pwn2Own) Tesla Model 3 VCSEC Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-265
- **ZDI-CAN:** ZDI-CAN-23800
- **Date:** 2025-04-30
- **CVE:** CVE-2025-2082
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model 3
- **Credit:** Synacktiv - Thomas Imbert - Vincent Dehors - David Berard
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-265/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Tesla Model 3 vehicles. Authentication is not required to exploit this vulnerability. The specific flaw exists within the VCSEC module. By manipulating the certificate response sent from the Tire Pressure Monitoring System (TPMS), an attacker can trigger an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the VCSEC module and send arbitrary messages to the vehicle CAN bus.

## Additional Details

Fixed in Firmware Version 2024.14

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated

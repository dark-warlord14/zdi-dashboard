# ZDI-25-262: (Pwn2Own) Tesla Model S Iris Modem QCMAP_ConnectionManager Improper Input Validation Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-262
- **ZDI-CAN:** ZDI-CAN-23199
- **Date:** 2025-04-30
- **CVE:** CVE-2024-13943
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model S
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-262/
## Vulnerability Details

This vulnerability allows local attackers to escape the sandbox on affected affected Tesla Model S vehicles. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the QCMAP_ConnectionManager component. An attacker can abuse the service to assign LAN addresses to the WWAN. An attacker can leverage this vulnerability to access network services that were only intended to be exposed to the internal LAN.

## Additional Details

Fixed in Firmware Version 2024.8

## Disclosure Timeline

- 2024-02-28 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated

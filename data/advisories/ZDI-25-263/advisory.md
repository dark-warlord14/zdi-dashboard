# ZDI-25-263: (Pwn2Own) Tesla Model S oFono Unnecessary Privileges Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-263
- **ZDI-CAN:** ZDI-CAN-23200
- **Date:** 2025-04-30
- **CVE:** CVE-2024-6030
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model S
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-263/
## Vulnerability Details

This vulnerability allows local attackers to escape the sandbox on affected Tesla Model S vehicles. An attacker must first obtain the ability to execute code within the sandbox on the target system in order to exploit this vulnerability. The specific flaw exists within the oFono process. The process allows an attacker to modify interfaces. An attacker can leverage this vulnerability to bypass the iptables network sandbox.

## Additional Details

Fixed in Firmware Version 2024.8

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated

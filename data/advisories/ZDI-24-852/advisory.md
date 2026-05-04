# ZDI-24-852: (Pwn2Own) Autel MaxiCharger AC Elite Business C50 BLE Hardcoded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-852
- **ZDI-CAN:** ZDI-CAN-23196
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23958
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Autel
- **Affected Products:** MaxiCharger AC Elite Business C50
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-852/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Autel MaxiCharger AC Elite Business C50 charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the BLE AppAuthenRequest command handler. The handler uses hardcoded credentials as a fallback in case of an authentication request failure. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in US Firmware v1.35.00 and EU Firmware v1.50.00.

## Disclosure Timeline

- 2024-02-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

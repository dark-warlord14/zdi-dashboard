# ZDI-24-851: (Pwn2Own) Autel MaxiCharger AC Elite Business C50 BLE AppChargingControl Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-851
- **ZDI-CAN:** ZDI-CAN-23194
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23959
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autel
- **Affected Products:** MaxiCharger AC Elite Business C50
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-851/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Autel MaxiCharger AC Elite Business C50 charging stations. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the AppChargingControl BLE command. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in US Firmware v1.35.00 and EU Firmware v1.50.00.

## Disclosure Timeline

- 2024-02-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

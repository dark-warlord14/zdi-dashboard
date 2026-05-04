# ZDI-24-1154: Autel MaxiCharger AC Elite Business C50 AppAuthenExchangeRandomNum Stack-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1154
- **ZDI-CAN:** ZDI-CAN-23384
- **Date:** 2024-08-20
- **CVE:** CVE-2024-7795
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autel
- **Affected Products:** MaxiCharger AC Elite Business C50
- **Credit:** Midnight Blue / PHP Hooligans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1154/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Autel MaxiCharger AC Elite Business C50 EV chargers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the AppAuthenExchangeRandomNum BLE command. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in firmware (EU firmware v1.51.00, US firmware v1.36.00)

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-20 - Coordinated public release of advisory
- 2024-08-20 - Advisory Updated

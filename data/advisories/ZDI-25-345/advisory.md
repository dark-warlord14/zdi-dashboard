# ZDI-25-345: (Pwn2Own) Autel MaxiCharger AC Wallbox Commercial ble_process_esp32_msg Misinterpretation of Input Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-345
- **ZDI-CAN:** ZDI-CAN-26368
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5826
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Autel
- **Affected Products:** Autel MaxiCharger AC Wallbox Commercial
- **Credit:** Quarkslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-345/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to inject arbitrary AT commands on affected installations of Autel MaxiCharger AC Wallbox Commercial charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ble_process_esp32_msg function. The issue results from misinterpretation of input data. An attacker can leverage this vulnerability to execute AT commands in the context of the device.

## Additional Details

Fixed in American Standard: V1.39.51 and European Standard: V1.56.51

## Disclosure Timeline

- 2025-05-12 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

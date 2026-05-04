# ZDI-25-344: (Pwn2Own) Autel MaxiCharger AC Wallbox Commercial Firmware Downgrade Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-344
- **ZDI-CAN:** ZDI-CAN-26354
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5825
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autel
- **Affected Products:** Autel MaxiCharger AC Wallbox Commercial
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-344/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Autel MaxiCharger AC Wallbox Commercial charging stations. An attacker must first obtain the ability to pair a malicious Bluetooth device with the target system in order to exploit this vulnerability. The specific flaw exists within the firmware update process. The issue results from the lack of proper validation of a firmware image before using it to perform an upgrade. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device.

## Additional Details

Fixed in American Standard: V1.39.51 and European Standard: V1.56.51

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

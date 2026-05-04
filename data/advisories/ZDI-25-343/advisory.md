# ZDI-25-343: (Pwn2Own) Autel MaxiCharger AC Wallbox Commercial Origin Validation Error Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-343
- **ZDI-CAN:** ZDI-CAN-26353
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5824
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Autel
- **Affected Products:** Autel MaxiCharger AC Wallbox Commercial
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-343/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Autel MaxiCharger AC Wallbox Commercial. An attacker must first obtain the ability to pair a malicious Bluetooth device with the target system in order to exploit this vulnerability. The specific flaw exists within the handling of bluetooth pairing requests. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in American Standard: V1.39.51 and European Standard: V1.56.51

## Disclosure Timeline

- 2025-05-28 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

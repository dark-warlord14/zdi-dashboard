# ZDI-25-327: (0Day) (Pwn2Own) WOLFBOX Level 2 EV Charger LAN OTA Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-327
- **ZDI-CAN:** ZDI-CAN-26349
- **Date:** 2025-06-06
- **CVE:** CVE-2025-5748
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WOLFBOX
- **Affected Products:** Level 2 EV Charger
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-327/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of WOLFBOX Level 2 EV Charger. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Tuya communications module software. The issue results from the exposure of a method allowing the upload of crafted software images to the module. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

ZDI made several attempts to contact the vendor using the contact information on their website, as well as trying to reach them on various social platforms which yielded no response. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-06-06 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated

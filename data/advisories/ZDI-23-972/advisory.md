# ZDI-23-972: (Pwn2Own) Tesla Model 3 Gateway Firmware Signature Validation Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-972
- **ZDI-CAN:** ZDI-CAN-20734
- **Date:** 2023-07-18
- **CVE:** CVE-2023-32156
- **CVSS:** 9.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model 3
- **Credit:** David BERARD (@_p0ly_) and Vincent DEHORS (@vdehors) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-972/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Tesla Model 3 vehicles. An attacker must first obtain the ability to execute privileged code on the Tesla infotainment system in order to exploit this vulnerability. The specific flaw exists within the handling of firmware updates. The issue results from improper error-handling during the update process. An attacker can leverage this vulnerability to execute code in the context of Tesla's Gateway ECU.

## Additional Details

Fixed in 2023.12 firmware release.

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-07-18 - Coordinated public release of advisory

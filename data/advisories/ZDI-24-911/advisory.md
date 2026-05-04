# ZDI-24-911: SolarWinds Access Rights Manager UserScriptHumster Exposed Dangerous Method Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-911
- **ZDI-CAN:** ZDI-CAN-22712
- **Date:** 2024-07-18
- **CVE:** CVE-2024-23470
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-911/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Access Rights Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UserScriptHumster class. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2024-3_release_notes.htm

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-07-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

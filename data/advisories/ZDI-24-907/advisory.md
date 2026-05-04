# ZDI-24-907: SolarWinds Access Rights Manager ChangeHumster Exposed Dangerous Method Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-907
- **ZDI-CAN:** ZDI-CAN-23053
- **Date:** 2024-07-18
- **CVE:** CVE-2024-23465
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-907/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of SolarWinds Access Rights Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ChangeHumster class. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to bypass Active Directory authentication.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2024-3_release_notes.htm

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-07-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

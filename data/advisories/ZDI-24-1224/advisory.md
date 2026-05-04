# ZDI-24-1224: SolarWinds Access Rights Manager JsonSerializationBinder Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1224
- **ZDI-CAN:** ZDI-CAN-24270
- **Date:** 2024-09-13
- **CVE:** CVE-2024-28991
- **CVSS:** 9.9
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1224/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Access Rights Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the JsonSerializationBinder class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2024-3-1_release_notes.htm

## Disclosure Timeline

- 2024-05-24 - Vulnerability reported to vendor
- 2024-09-13 - Coordinated public release of advisory
- 2024-09-13 - Advisory Updated

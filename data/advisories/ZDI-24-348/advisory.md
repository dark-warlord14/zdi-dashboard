# ZDI-24-348: SolarWinds Access Rights Manager openServerFileStream Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-348
- **ZDI-CAN:** ZDI-CAN-22739
- **Date:** 2024-03-28
- **CVE:** CVE-2024-23477
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** 07842c0e165d4d2d8733dd4eab48b3ed0f7afe38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-348/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Access Rights Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the openServerFileStream method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-3_release_notes.htm

## Disclosure Timeline

- 2023-12-23 - Vulnerability reported to vendor
- 2024-03-28 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

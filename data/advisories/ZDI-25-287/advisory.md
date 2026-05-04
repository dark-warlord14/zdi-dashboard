# ZDI-25-287: JetBrains TeamCity Diagnostics Data Directory Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-287
- **ZDI-CAN:** ZDI-CAN-25977
- **Date:** 2025-05-13
- **CVE:** CVE-2025-46618
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N
- **Affected Vendors:** JetBrains
- **Affected Products:** TeamCity
- **Credit:** Grigory Dorodnov of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary script on affected installations of JetBrains TeamCity. Minimal user interaction is required to exploit this vulnerability. The specific flaw exists within the handling of filenames in the diagnostics functionality. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of arbitrary script. An attacker can leverage this vulnerability to execute script in the context of a target user.

## Additional Details

JetBrains has issued an update to correct this vulnerability. More details can be found at: https://www.jetbrains.com/help/teamcity/2025.03/teamcity-2025-03-1-release-notes.html#Security

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-05-13 - Coordinated public release of advisory
- 2025-05-13 - Advisory Updated

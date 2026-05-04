# ZDI-24-916: SolarWinds Access Rights Manager AddReportResult Directory Traversal Arbitrary File Deletion and Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-916
- **ZDI-CAN:** ZDI-CAN-23061
- **Date:** 2024-07-18
- **CVE:** CVE-2024-23475
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-916/
## Vulnerability Details

This vulnerability allows remote attackers to read and delete arbitrary files on affected installations of SolarWinds Access Rights Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AddReportResult method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to read and delete files in the context of a highly privileged domain user.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2024-3_release_notes.htm

## Disclosure Timeline

- 2024-01-12 - Vulnerability reported to vendor
- 2024-07-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

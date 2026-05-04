# ZDI-24-171: SolarWinds Orion Platform AppendUpdate SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-171
- **ZDI-CAN:** ZDI-CAN-21894
- **Date:** 2024-02-15
- **CVE:** CVE-2023-50395
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the AppendUpdate method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/solarwinds_platform_2024-1_release_notes.htm

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2024-02-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

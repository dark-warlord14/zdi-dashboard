# ZDI-23-1762: SolarWinds Orion Platform VimChartInfo SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1762
- **ZDI-CAN:** ZDI-CAN-21962
- **Date:** 2023-12-05
- **CVE:** CVE-2023-40056
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Alex Birnberg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1762/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the VimChartInfo class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/solarwinds_platform_2023-4-2_release_notes.htm

## Disclosure Timeline

- 2023-10-19 - Vulnerability reported to vendor
- 2023-12-05 - Coordinated public release of advisory

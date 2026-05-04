# ZDI-23-1443: SolarWinds Orion Platform UpdateActionsProperties Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1443
- **ZDI-CAN:** ZDI-CAN-21097
- **Date:** 2023-09-19
- **CVE:** CVE-2023-23845
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1443/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the UpdateActionsProperties method. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/solarwinds_platform_2023-3-1_release_notes.htm

## Disclosure Timeline

- 2023-05-11 - Vulnerability reported to vendor
- 2023-09-19 - Coordinated public release of advisory

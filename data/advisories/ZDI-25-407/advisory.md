# ZDI-25-407: SolarWinds Web Help Desk AjaxProxy Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-407
- **ZDI-CAN:** ZDI-CAN-25346
- **Date:** 2025-06-17
- **CVE:** CVE-2024-28988
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Web Help Desk
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-407/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Web Help Desk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AjaxProxy. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/whd/content/release_notes/whd_12-8-3-hotfix-3_release_notes.htm

## Disclosure Timeline

- 2024-09-10 - Vulnerability reported to vendor
- 2025-06-17 - Coordinated public release of advisory
- 2025-06-17 - Advisory Updated

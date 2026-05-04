# ZDI-25-906: SolarWinds Web Help Desk AjaxProxy Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-906
- **ZDI-CAN:** ZDI-CAN-26042
- **Date:** 2025-09-23
- **CVE:** CVE-2025-26399
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Web Help Desk
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-906/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Web Help Desk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AjaxProxy class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2025-26399

## Disclosure Timeline

- 2025-08-26 - Vulnerability reported to vendor
- 2025-09-23 - Coordinated public release of advisory
- 2025-09-23 - Advisory Updated

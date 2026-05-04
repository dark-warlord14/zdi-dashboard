# ZDI-21-1245: SolarWinds Orion Platform ActionPluginBaseView Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1245
- **ZDI-CAN:** ZDI-CAN-13845
- **Date:** 2021-10-28
- **CVE:** CVE-2021-35215
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Jangggggg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1245/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the ActionPluginBaseView class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35215

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory

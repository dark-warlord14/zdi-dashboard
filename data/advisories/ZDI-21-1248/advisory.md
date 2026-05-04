# ZDI-21-1248: SolarWinds Patch Manager Chart Endpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1248
- **ZDI-CAN:** ZDI-CAN-14190
- **Date:** 2021-10-28
- **CVE:** CVE-2021-35218
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Patch Manager
- **Credit:** Jangggggg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1248/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Patch Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Chart endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35218

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory

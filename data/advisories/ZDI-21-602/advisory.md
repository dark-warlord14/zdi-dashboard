# ZDI-21-602: SolarWinds Network Performance Monitor FromJson Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-602
- **ZDI-CAN:** ZDI-CAN-12213
- **Date:** 2021-09-20
- **CVE:** CVE-2021-31474
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-602/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the SolarWinds.Serialization library. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/orion_platform_2020-2-5_release_notes.htm

## Disclosure Timeline

- 2020-12-11 - Vulnerability reported to vendor
- 2021-09-20 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated

# ZDI-23-1560: SolarWinds Access Rights Manager IFormTemplate Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1560
- **ZDI-CAN:** ZDI-CAN-21375
- **Date:** 2023-10-19
- **CVE:** CVE-2023-35180
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1560/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Access Rights Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the deserialization of JSON data sent to the API via TCP port 443. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-1_release_notes.htm

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-10-19 - Coordinated public release of advisory

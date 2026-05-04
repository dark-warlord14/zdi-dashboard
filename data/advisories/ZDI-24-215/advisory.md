# ZDI-24-215: SolarWinds Security Event Manager AMF Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-215
- **ZDI-CAN:** ZDI-CAN-22955
- **Date:** 2024-03-01
- **CVE:** CVE-2024-0692
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Security Event Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-215/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Security Event Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the AMF deserialization endpoints. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/sem/content/release_notes/sem_2023-4-1_release_notes.htm

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-03-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

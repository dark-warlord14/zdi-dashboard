# ZDI-24-454: SolarWinds Access Rights Manager Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-454
- **ZDI-CAN:** ZDI-CAN-23059
- **Date:** 2024-05-15
- **CVE:** CVE-2024-23473
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:L
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-454/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of SolarWinds Access Rights Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of a RabbitMQ instance. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass RabbitMQ authentication.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2023-2-4_release_notes.htm

## Disclosure Timeline

- 2024-01-12 - Vulnerability reported to vendor
- 2024-05-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

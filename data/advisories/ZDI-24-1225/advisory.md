# ZDI-24-1225: SolarWinds Access Rights Manager Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1225
- **ZDI-CAN:** ZDI-CAN-24271
- **Date:** 2024-09-13
- **CVE:** CVE-2024-28990
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** SolarWinds
- **Affected Products:** Access Rights Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1225/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of SolarWinds Access Rights Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of a RabbitMQ instance. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass RabbitMQ authentication.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2024-3-1_release_notes.htm

## Disclosure Timeline

- 2024-05-24 - Vulnerability reported to vendor
- 2024-09-13 - Coordinated public release of advisory
- 2024-09-13 - Advisory Updated

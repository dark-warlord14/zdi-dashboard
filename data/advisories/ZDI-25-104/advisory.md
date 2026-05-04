# ZDI-25-104: SolarWinds Platform TestWebsiteUrl Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-104
- **ZDI-CAN:** ZDI-CAN-25334
- **Date:** 2025-03-03
- **CVE:** CVE-2024-52606
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** SolarWinds
- **Affected Products:** Platform
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-104/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of SolarWinds Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the TestWebsiteUrl method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2024-52606

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-03-03 - Coordinated public release of advisory
- 2025-03-03 - Advisory Updated

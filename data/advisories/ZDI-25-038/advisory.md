# ZDI-25-038: Ivanti Endpoint Manager Improper Input Validation AlertService Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-038
- **ZDI-CAN:** ZDI-CAN-25420
- **Date:** 2025-01-19
- **CVE:** CVE-2024-13165
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-038/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AlertService. The issue results from the lack of proper validation of the length of user-supplied data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-January-2025-for-EPM-2024-and-EPM-2022-SU6

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated

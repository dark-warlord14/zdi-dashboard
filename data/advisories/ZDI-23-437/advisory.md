# ZDI-23-437: ManageEngine ADSelfService Plus DomainUserSSPLogonAuth Improper Input Validation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-437
- **ZDI-CAN:** ZDI-CAN-20008
- **Date:** 2023-04-12
- **CVE:** CVE-2023-28342
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ADSelfService Plus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-437/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of ManageEngine ADSelfService Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DomainUserSSPLogonAuth method. The issue results from improper input validation. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/self-service-password/advisory/CVE-2023-28342.html

## Disclosure Timeline

- 2023-02-17 - Vulnerability reported to vendor
- 2023-04-12 - Coordinated public release of advisory

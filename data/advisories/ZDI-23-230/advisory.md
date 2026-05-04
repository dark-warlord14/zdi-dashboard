# ZDI-23-230: ManageEngine ServiceDesk Plus ImageUploadServlet Improper Input Validation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-230
- **ZDI-CAN:** ZDI-CAN-19537
- **Date:** 2023-03-09
- **CVE:** CVE-2023-26601
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ServiceDesk Plus
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-230/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of ManageEngine ServiceDesk Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the ImageUploadServlet. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/service-desk/CVE-2023-26601.html

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-03-09 - Coordinated public release of advisory

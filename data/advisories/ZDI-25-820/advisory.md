# ZDI-25-820: (0Day) Microsoft SharePoint IsAuthorizedType Deserialization of Untrusted Data Information Disclosure and Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-820
- **ZDI-CAN:** ZDI-CAN-24831
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-820/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information or create a denial-of-service condition on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the SPNoCodeXomlCompiler.IsAuthorizedType method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to disclose information or create a denial-of-service condition on the system.

## Additional Details

07/12/24 – ZDI reported the vulnerability to the vendor. 07/15/24 – The vendor acknowledged the report. 07/18/24 – The vendor asked for additional details. 07/21/24 – ZDI followed up and provided more information about the case. 09/12/24 – The vendor assessed the case as not meeting the bar servicing. 07/30/25 – ZDI Informed the vendor that we plan to publish the case as a zero-day advisory on 08/06/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated

# ZDI-25-822: (0Day) Microsoft SharePoint GetTransformer Unsafe Reflection Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-822
- **ZDI-CAN:** ZDI-CAN-25207
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-822/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the GetTransformer method. The issue results from the lack of proper validation of user-supplied data, which can result in unsafe reflection. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

08/222/24 – ZDI reported the vulnerability to the vendor. 08/23/24 – The vendor acknowledged the report. 09/25/24 – The vendor confirmed the reported behavior. 10/03/24 – The vendor assessed the case as not meeting the bar servicing. 07/30/25 – ZDI Informed the vendor that we plan to publish the case as a zero-day advisory on 08/06/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-08-22 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated

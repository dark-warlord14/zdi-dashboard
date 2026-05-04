# ZDI-25-816: (0Day) Microsoft Azure AP5GC gNB-ID Use of Multiple Resources with Duplicate Identifier Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-816
- **ZDI-CAN:** ZDI-CAN-23960
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Richard Y Lin, Salim S. I. (CTOne/TrendMicro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-816/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Azure. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the gNB-ID provided to the AP5GC endpoint. The product expects a unique id for each resource but does not enforce it correctly. An attacker can leverage this vulnerability to create a denial-of-service condition on connected clients.

## Additional Details

04/25/24 – ZDI reported the vulnerability to the vendor. 04/25/24 – The vendor acknowledged the report. 05/15/24 – The vendor confirmed the reported behavior. 07/26/24 – The vendor states they are working on a response for this case. 08/16/24 – The vendor assessed the case as not meeting the bar servicing. 07/30/25 – ZDI Informed the vendor that we plan to publish the case as a zero-day advisory on 08/06/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated

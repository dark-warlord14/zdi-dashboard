# ZDI-25-468: GFI Archiver Telerik Web UI Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-468
- **ZDI-CAN:** ZDI-CAN-26061
- **Date:** 2025-07-03
- **CVE:** CVE-2019-18935 , CVE-2017-11317 , CVE-2014-2217
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GFI
- **Affected Products:** Archiver
- **Credit:** anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-468/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GFI Archiver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from the use of a vulnerable version of Telerik Web UI. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in GFI Archiver 15.9 https://gfi.ai/products-and-solutions/network-security-solutions/archiver/resources/documentation/product-releases

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-07-03 - Coordinated public release of advisory
- 2025-07-03 - Advisory Updated

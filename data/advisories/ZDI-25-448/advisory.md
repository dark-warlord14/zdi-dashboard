# ZDI-25-448: (0Day) Mescius ActiveReports.NET ReadValue Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-448
- **ZDI-CAN:** ZDI-CAN-25246
- **Date:** 2025-06-27
- **CVE:** CVE-2025-6810
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mescius
- **Affected Products:** ActiveReports.NET
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-448/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mescius ActiveReports.NET. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementation of the ReadValue method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

11/08/24 – ZDI submitted the report to the vendor 11/08/24 – the vendor acknowledged the receipt of the report 01/07/25 – the vendor communicated that the reported behaviour was by design 01/09/25 – ZDI replied with an evidence form the product’s documentation 01/15/25 – the vendor confirmed that there wouldn’t be a security issue if the report uploading task were done by internal trusted developers 06/19/25 - ZDI notified the vendor of the intention to publish the case as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2024-11-08 - Vulnerability reported to vendor
- 2025-06-27 - Coordinated public release of advisory
- 2025-12-19 - Advisory Updated

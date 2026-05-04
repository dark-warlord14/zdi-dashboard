# ZDI-25-813: (0Day) Microsoft PowerShell TryModuleAutoLoading Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-813
- **ZDI-CAN:** ZDI-CAN-23444
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PowerShell
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-813/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft PowerShell. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the TryModuleAutoLoading method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

02/21/24 – ZDI reported the vulnerability to the vendor. 02/23/24 – The vendor acknowledged the report. 05/24/24 – ZDI asked for an update. 06/08/24 – The vendor states there is no security impact. 07/30/25 – ZDI Informed the vendor that we plan to publish the case as a zero-day advisory on 08/06/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated

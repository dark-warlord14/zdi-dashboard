# ZDI-25-775: (0Day) Google Chrome SwiftShader Out-Of-Bound Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-775
- **ZDI-CAN:** ZDI-CAN-25494
- **Date:** 2025-08-05
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-775/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the WebGPU API. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the Chrome browser GPU process.

## Additional Details

10/03/24 – ZDI reported the vulnerability to the vendor. 10/03/24 – The vendor acknowledged the report. 10/07/24 – The vendor asked for additional details. 11/12/24 – ZDI provided the requested details. 12/03/24 – The vendor states that there is no security impact. 03/18/25 – ZDI asked for an update and expressed our intent to publish the case as a zero-day advisory. 03/19/25 – The vendor states their assessment remains unchanged. 03/19/25 – The ZDI informed the vendor that we believe this should be serviced, and that we plan to publish the case as a zero-day advisory. 07/31/25 – After careful review the ZDI decided that this case should be disclosed publicly on 08/05/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-08-05 - Coordinated public release of advisory
- 2025-08-05 - Advisory Updated

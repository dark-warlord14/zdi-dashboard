# ZDI-25-821: (0Day) Microsoft Windows Internet Explorer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-821
- **ZDI-CAN:** ZDI-CAN-24974
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz) - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-821/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the registration of Internet Explorer as a COM-creatable object. Although Internet Explorer is a retired component, an attacker can launch it via COM from an Internet Shortcut file or other vector. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

07/18/24 – ZDI reported the vulnerability to the vendor 07/18/24 – the vendor acknowledged the receipt of the report 05/02/24 – the vendor communicated that the reported behaviour was by design and did not meet the bar for immediate servicing 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-07-18 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated

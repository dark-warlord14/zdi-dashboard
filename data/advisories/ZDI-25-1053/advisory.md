# ZDI-25-1053: (0Day) Microsoft SharePoint Calendar Overlay Hyperlink Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1053
- **ZDI-CAN:** ZDI-CAN-27955
- **Date:** 2025-12-10
- **CVE:** N/A
- **CVSS:** 3.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Vladislav Berghici of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1053/
## Vulnerability Details

This vulnerability allows remote attackers to inject unexpected hyperlinks on affected installations of Microsoft SharePoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of calendar overlays. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary hyperlink. An attacker can leverage this vulnerability to redirect a target user to a deceptive, untrusted page.

## Additional Details

08/28/25 - ZDI reported the vulnerability to the vendor 08/29/25 – the vendor acknowledged the receipt of the report 09/25/25 – the vendor communicated that the reported behavior did not meet the bar for immediate servicing 11/26/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory on 12/10/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-28 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated

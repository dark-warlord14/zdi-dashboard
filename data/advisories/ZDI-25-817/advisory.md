# ZDI-25-817: (0Day) Microsoft Edge PDF NTLM Response Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-817
- **ZDI-CAN:** ZDI-CAN-23584
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** @0xwarlok
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-817/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of links within rendered PDF documents. The issue results from not respecting the Mark-of-the-Web on PDF documents saved from untrusted locations. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

06/05/24 – ZDI reported the vulnerability to the vendor. 06/05/24 – The vendor acknowledged the report. 06/11/24 – The vendor assessed the case as not meeting the bar servicing. 07/30/25 – ZDI Informed the vendor that we plan to publish the case as a zero-day advisory on 08/06/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated

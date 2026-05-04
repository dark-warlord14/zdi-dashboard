# ZDI-23-1143: PDF-XChange Editor Net.HTTP.requests Exposed Dangerous Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1143
- **ZDI-CAN:** ZDI-CAN-20211
- **Date:** 2023-08-17
- **CVE:** CVE-2023-39505
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1143/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Net.HTTP.requests method. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

Fixed in PDF-XChange Editor V9 (9.5.368) and V10 (10.0.1) https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-08-17 - Coordinated public release of advisory

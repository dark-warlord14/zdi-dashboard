# ZDI-23-1134: PDF-XChange Editor PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1134
- **ZDI-CAN:** ZDI-CAN-19636
- **Date:** 2023-08-17
- **CVE:** CVE-2023-39490
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** hades_kito
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. Crafted data in a PDF file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in PDF-XChange Editor V9 (9.5.368) and V10 (10.0.1) https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2023-01-04 - Vulnerability reported to vendor
- 2023-08-17 - Coordinated public release of advisory

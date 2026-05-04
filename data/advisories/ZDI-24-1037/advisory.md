# ZDI-24-1037: PDF-XChange Editor PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1037
- **ZDI-CAN:** ZDI-CAN-23550
- **Date:** 2024-07-31
- **CVE:** CVE-2024-7352
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Build 10.3.0.386 https://www.pdf-xchange.com/product/pdf-xchange-editor/history#Build%2010.3.0.386

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2024-07-31 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

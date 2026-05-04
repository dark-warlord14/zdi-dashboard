# ZDI-23-1149: PDF-XChange Editor JavaScript String Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1149
- **ZDI-CAN:** ZDI-CAN-20730
- **Date:** 2023-08-17
- **CVE:** CVE-2023-40472
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1149/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of strings. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in PDF-XChange Editor V9 (9.5.368) and V10 (10.0.1) https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-08-17 - Coordinated public release of advisory

# ZDI-25-070: PDF-XChange Editor RTF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-070
- **ZDI-CAN:** ZDI-CAN-25421
- **Date:** 2025-01-31
- **CVE:** CVE-2025-0903
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RTF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 10.4.2.390 https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2024-10-01 - Vulnerability reported to vendor
- 2025-01-31 - Coordinated public release of advisory
- 2025-01-31 - Advisory Updated

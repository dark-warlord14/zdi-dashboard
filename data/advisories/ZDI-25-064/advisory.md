# ZDI-25-064: PDF-XChange Editor XPS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-064
- **ZDI-CAN:** ZDI-CAN-25678
- **Date:** 2025-01-31
- **CVE:** CVE-2025-0909
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-064/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XPS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in version 10.5.0.393 https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2024-11-13 - Vulnerability reported to vendor
- 2025-01-31 - Coordinated public release of advisory
- 2025-01-31 - Advisory Updated

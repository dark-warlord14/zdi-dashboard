# ZDI-24-204: PDF-XChange Editor XPS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-204
- **ZDI-CAN:** ZDI-CAN-22276
- **Date:** 2024-02-23
- **CVE:** CVE-2024-27326
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-204/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XPS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

fixed in version 10.1.2.382: https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2024-02-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

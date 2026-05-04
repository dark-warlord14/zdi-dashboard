# ZDI-25-065: PDF-XChange Editor U3D File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-065
- **ZDI-CAN:** ZDI-CAN-25748
- **Date:** 2025-01-31
- **CVE:** CVE-2025-0910
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 10.5.0.393 https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-01-31 - Coordinated public release of advisory
- 2025-01-31 - Advisory Updated

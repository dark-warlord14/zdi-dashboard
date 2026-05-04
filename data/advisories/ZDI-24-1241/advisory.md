# ZDI-24-1241: PDF-XChange Editor U3D File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1241
- **ZDI-CAN:** ZDI-CAN-24213
- **Date:** 2024-09-17
- **CVE:** CVE-2024-8818
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1241/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 10.3.1.387 ( https://www.pdf-xchange.com/index.php/support/security-bulletins.html )

## Disclosure Timeline

- 2024-05-19 - Vulnerability reported to vendor
- 2024-09-17 - Coordinated public release of advisory
- 2024-09-17 - Advisory Updated

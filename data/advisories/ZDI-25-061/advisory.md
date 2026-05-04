# ZDI-25-061: PDF-XChange Editor AcroForm Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-061
- **ZDI-CAN:** ZDI-CAN-25349
- **Date:** 2025-01-31
- **CVE:** CVE-2025-0899
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-061/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AcroForms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 10.4.1.389 https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2024-09-13 - Vulnerability reported to vendor
- 2025-01-31 - Coordinated public release of advisory
- 2025-01-31 - Advisory Updated

# ZDI-25-324: Sante DICOM Viewer Pro DCM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-324
- **ZDI-CAN:** ZDI-CAN-26168
- **Date:** 2025-06-03
- **CVE:** CVE-2025-5481
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** D4m0n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-324/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DCM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 14.2.0 of Sante DICOM Viewer Pro

## Disclosure Timeline

- 2025-02-20 - Vulnerability reported to vendor
- 2025-06-03 - Coordinated public release of advisory
- 2025-06-03 - Advisory Updated

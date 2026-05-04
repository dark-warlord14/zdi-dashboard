# ZDI-26-104: Sante DICOM Viewer Pro DCM File Parsing Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-104
- **ZDI-CAN:** ZDI-CAN-28129
- **Date:** 2026-02-13
- **CVE:** CVE-2026-2034
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DCM files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 14.2.7.

## Disclosure Timeline

- 2025-09-25 - Vulnerability reported to vendor
- 2026-02-13 - Coordinated public release of advisory
- 2026-02-13 - Advisory Updated

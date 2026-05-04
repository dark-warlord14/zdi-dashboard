# ZDI-22-256: Sante DICOM Viewer Pro J2K File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-256
- **ZDI-CAN:** ZDI-CAN-15161
- **Date:** 2022-02-02
- **CVE:** CVE-2022-24064
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-256/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of J2K images. Crafted data in a J2K file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in DICOM Viewer Pro version 11.9.2

## Disclosure Timeline

- 2021-09-17 - Vulnerability reported to vendor
- 2022-02-02 - Coordinated public release of advisory

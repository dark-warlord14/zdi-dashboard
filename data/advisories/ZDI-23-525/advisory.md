# ZDI-23-525: Sante DICOM Viewer Pro J2K File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-525
- **ZDI-CAN:** ZDI-CAN-15628
- **Date:** 2023-05-04
- **CVE:** CVE-2023-32133
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-525/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of J2K images. Crafted data in a J2K image can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Sante DICOM Editor 7.8.12 and Sante DICOM Viewer Pro 11.8.12

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory

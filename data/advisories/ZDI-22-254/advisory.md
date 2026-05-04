# ZDI-22-254: Sante DICOM Viewer Pro JP2 File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-254
- **ZDI-CAN:** ZDI-CAN-15104
- **Date:** 2022-02-02
- **CVE:** CVE-2022-24062
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-254/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JP2 files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in DICOM Viewer Pro version 11.9.2

## Disclosure Timeline

- 2021-08-27 - Vulnerability reported to vendor
- 2022-02-02 - Coordinated public release of advisory

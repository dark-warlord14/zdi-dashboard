# ZDI-23-855: Sante DICOM Viewer Pro DCM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-855
- **ZDI-CAN:** ZDI-CAN-21126
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34296
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-855/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DCM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in 12.2.4.

## Disclosure Timeline

- 2023-05-17 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory

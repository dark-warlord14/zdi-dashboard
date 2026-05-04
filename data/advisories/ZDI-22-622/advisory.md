# ZDI-22-622: Sante DICOM Viewer Pro J2K File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-622
- **ZDI-CAN:** ZDI-CAN-16679
- **Date:** 2022-04-28
- **CVE:** CVE-2022-28668
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** DICOM Viewer Pro
- **Credit:** Eunice
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-622/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante DICOM Viewer Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of J2K files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in DICOM Viewer Pro version 11.9.3

## Disclosure Timeline

- 2022-04-01 - Vulnerability reported to vendor
- 2022-04-28 - Coordinated public release of advisory

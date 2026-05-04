# ZDI-21-306: SAP 3D Visual Enterprise Viewer SVG File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-306
- **ZDI-CAN:** ZDI-CAN-12139
- **Date:** 2021-03-15
- **CVE:** CVE-2021-27589
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** xina1i at SecZone
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-306/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SVG files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in SAP 3D Visual Enterprise Viewer 9.0 FP10 MP2

## Disclosure Timeline

- 2020-11-18 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory

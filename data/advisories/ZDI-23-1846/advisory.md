# ZDI-23-1846: Trimble SketchUp Viewer SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1846
- **ZDI-CAN:** ZDI-CAN-21800
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50196
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1846/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

fixed in windows version 23.2.101 and mac version 23.2.102

## Disclosure Timeline

- 2023-07-26 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory

# ZDI-24-1376: Trimble SketchUp Viewer SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1376
- **ZDI-CAN:** ZDI-CAN-24098
- **Date:** 2024-10-11
- **CVE:** CVE-2024-9715
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1376/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 2024.0.2 https://help.sketchup.com/en/release-notes/sketchup-202402

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated

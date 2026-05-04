# ZDI-25-1198: Trimble SketchUp SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1198
- **ZDI-CAN:** ZDI-CAN-27769
- **Date:** 2025-12-29
- **CVE:** CVE-2025-15062
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp
- **Credit:** Kevin Salapatek of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1198/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in SketchUp 2026 version 26.0.429

## Disclosure Timeline

- 2025-07-31 - Vulnerability reported to vendor
- 2025-12-29 - Coordinated public release of advisory
- 2025-12-29 - Advisory Updated

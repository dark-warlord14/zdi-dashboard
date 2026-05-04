# ZDI-24-187: Trimble SketchUp SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-187
- **ZDI-CAN:** ZDI-CAN-19112
- **Date:** 2024-02-21
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-187/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in SketchUp SDK Security Patch 2023-0-421 https://help.sketchup.com/en/release-notes/sketchup-desktop-202302

## Disclosure Timeline

- 2022-11-11 - Vulnerability reported to vendor
- 2024-02-21 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

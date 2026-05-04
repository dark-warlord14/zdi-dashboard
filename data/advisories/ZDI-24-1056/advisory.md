# ZDI-24-1056: Trimble SketchUp SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1056
- **ZDI-CAN:** ZDI-CAN-19631
- **Date:** 2024-08-05
- **CVE:** CVE-2024-7510
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in SketchUp Version: 24.0.553.

## Disclosure Timeline

- 2023-01-11 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

# ZDI-24-700: Autodesk AutoCAD MODEL File Parsing Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-700
- **ZDI-CAN:** ZDI-CAN-23352
- **Date:** 2024-06-13
- **CVE:** CVE-2024-23141
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** AutoCAD
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-700/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MODEL files. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2024-0009

## Disclosure Timeline

- 2024-02-06 - Vulnerability reported to vendor
- 2024-06-13 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

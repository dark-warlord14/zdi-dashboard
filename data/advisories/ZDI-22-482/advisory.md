# ZDI-22-482: Autodesk AutoCAD TIF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-482
- **ZDI-CAN:** ZDI-CAN-15560
- **Date:** 2022-03-07
- **CVE:** CVE-2021-27036
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** AutoCAD
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-482/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF images. Crafted data in a TIF image can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0004

## Disclosure Timeline

- 2021-10-21 - Vulnerability reported to vendor
- 2022-03-07 - Coordinated public release of advisory
- 2022-07-14 - Advisory Updated

# ZDI-24-129: Autodesk AutoCAD MODEL File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-129
- **ZDI-CAN:** ZDI-CAN-20893
- **Date:** 2024-02-12
- **CVE:** CVE-2024-23128
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** AutoCAD
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MODEL files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.autodesk.com/trust/security-advisories/adsk-sa-2024-0002 https://www.autodesk.com/trust/security-advisories/adsk-sa-2024-0004

## Disclosure Timeline

- 2023-06-27 - Vulnerability reported to vendor
- 2024-02-12 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated

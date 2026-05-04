# ZDI-22-1315: Autodesk AutoCAD X_B File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1315
- **ZDI-CAN:** ZDI-CAN-17154
- **Date:** 2022-09-29
- **CVE:** CVE-2022-33884
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Autodesk
- **Affected Products:** AutoCAD
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1315/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X_B files. Crafted data in an X_B file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0020

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-09-29 - Coordinated public release of advisory

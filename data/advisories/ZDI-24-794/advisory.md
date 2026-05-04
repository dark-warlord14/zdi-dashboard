# ZDI-24-794: (0Day) Autodesk AutoCAD STP File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-794
- **ZDI-CAN:** ZDI-CAN-23409
- **Date:** 2024-06-18
- **CVE:** CVE-2024-23159
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** AutoCAD
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-794/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of STP files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2024-0010

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated

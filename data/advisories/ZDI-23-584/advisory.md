# ZDI-23-584: Autodesk 3DS Max USD File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-584
- **ZDI-CAN:** ZDI-CAN-20169
- **Date:** 2023-05-12
- **CVE:** CVE-2023-25009
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** 3DS Max
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-584/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk 3DS Max. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of USD files. Crafted data in a USD file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2023-0008

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-05-12 - Coordinated public release of advisory

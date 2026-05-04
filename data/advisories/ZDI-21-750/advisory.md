# ZDI-21-750: Autodesk Design Review TIF File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-750
- **ZDI-CAN:** ZDI-CAN-13322
- **Date:** 2021-06-22
- **CVE:** CVE-2021-27035
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** xina1i at SecZone
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-750/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF files. Crafted data in a TIF file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0003

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-06-22 - Coordinated public release of advisory

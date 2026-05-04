# ZDI-21-466: Autodesk FBX Review ZIP File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-466
- **ZDI-CAN:** ZDI-CAN-12229
- **Date:** 2021-04-23
- **CVE:** CVE-2021-27030
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** FBX Review
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-466/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk FBX Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ZIP files. When handling filenames specified within a ZIP file, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0001

## Disclosure Timeline

- 2021-01-21 - Vulnerability reported to vendor
- 2021-04-23 - Coordinated public release of advisory

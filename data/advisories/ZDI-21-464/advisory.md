# ZDI-21-464: Autodesk FBX Review FBX File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-464
- **ZDI-CAN:** ZDI-CAN-12211
- **Date:** 2021-04-23
- **CVE:** CVE-2021-27029
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** FBX Review
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-464/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk FBX Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FBX files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0001

## Disclosure Timeline

- 2021-01-21 - Vulnerability reported to vendor
- 2021-04-23 - Coordinated public release of advisory

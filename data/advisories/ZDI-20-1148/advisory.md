# ZDI-20-1148: SAP 3D Visual Enterprise Viewer FBX File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1148
- **ZDI-CAN:** ZDI-CAN-11265
- **Date:** 2020-09-10
- **CVE:** CVE-2020-6352
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FBX files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=557449700

## Disclosure Timeline

- 2020-06-26 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory

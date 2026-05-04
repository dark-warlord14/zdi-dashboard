# ZDI-20-1138: SAP 3D Visual Enterprise Viewer 3DM File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1138
- **ZDI-CAN:** ZDI-CAN-11089
- **Date:** 2020-09-10
- **CVE:** CVE-2020-6327
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1138/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 3DM files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=557449700

## Disclosure Timeline

- 2020-06-09 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory

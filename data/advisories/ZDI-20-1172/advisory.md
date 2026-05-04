# ZDI-20-1172: SAP 3D Visual Enterprise Viewer RLE File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1172
- **ZDI-CAN:** ZDI-CAN-11501
- **Date:** 2020-09-10
- **CVE:** CVE-2020-6361
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1172/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RLE files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=557449700

## Disclosure Timeline

- 2020-07-10 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory

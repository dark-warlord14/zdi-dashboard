# ZDI-22-958: SAP 3D Visual Enterprise Viewer EPS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-958
- **ZDI-CAN:** ZDI-CAN-16526
- **Date:** 2022-07-07
- **CVE:** CVE-2022-32238
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** insu of Diffense
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-958/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EPS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.sap.com/documents/2022/02/fa865ea4-167e-0010-bca6-c68f7e60039b.html https://www.sap.com/documents/2022/02/089613a0-167e-0010-bca6-c68f7e60039b.html

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2022-07-07 - Coordinated public release of advisory

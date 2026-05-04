# ZDI-23-746: SAP 3D Visual Enterprise Viewer JT File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-746
- **ZDI-CAN:** ZDI-CAN-16666
- **Date:** 2023-05-31
- **CVE:** CVE-2022-26107
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** insu of 78 Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-746/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://d.dam.sap.com/a/3Hat4sC/2022%2012%20Patch%20Day%20Blog%20V9.0.pdf?rc=10

## Disclosure Timeline

- 2022-03-30 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory

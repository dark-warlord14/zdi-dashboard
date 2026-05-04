# ZDI-21-016: SAP 3D Visual Enterprise Viewer PCX File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-016
- **ZDI-CAN:** ZDI-CAN-12314
- **Date:** 2021-01-12
- **CVE:** CVE-2021-21463
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PCX files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

fixed with the latest patch release VE Viewer 9.0 FP10

## Disclosure Timeline

- 2020-11-18 - Vulnerability reported to vendor
- 2021-01-12 - Coordinated public release of advisory

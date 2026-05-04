# ZDI-25-508: IrfanView CADImage Plugin DXF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-508
- **ZDI-CAN:** ZDI-CAN-26129
- **Date:** 2025-07-08
- **CVE:** CVE-2025-7260
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** IrfanView
- **Affected Products:** IrfanView
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-508/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IrfanView CADImage Plugin. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in IrfanView CADImage Plugin version 4.72

## Disclosure Timeline

- 2025-02-11 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated

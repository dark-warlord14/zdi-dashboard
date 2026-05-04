# ZDI-25-494: IrfanView CADImage Plugin DWG File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-494
- **ZDI-CAN:** ZDI-CAN-26072
- **Date:** 2025-07-08
- **CVE:** CVE-2025-7233
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** IrfanView
- **Affected Products:** IrfanView
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-494/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of IrfanView CADImage Plugin. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in IrfanView CADImage Plugin version 4.72

## Disclosure Timeline

- 2025-02-20 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated

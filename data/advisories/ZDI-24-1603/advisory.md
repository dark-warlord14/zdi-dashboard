# ZDI-24-1603: IrfanView DXF File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1603
- **ZDI-CAN:** ZDI-CAN-22184
- **Date:** 2024-11-21
- **CVE:** CVE-2024-11508
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** IrfanView
- **Affected Products:** IrfanView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1603/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IrfanView. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in IrfanView version 4.70 with plugins version 4.70

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2024-11-21 - Coordinated public release of advisory
- 2024-11-21 - Advisory Updated

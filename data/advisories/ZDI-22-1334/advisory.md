# ZDI-22-1334: PDF-XChange Editor U3D File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1334
- **ZDI-CAN:** ZDI-CAN-18282
- **Date:** 2022-10-07
- **CVE:** CVE-2022-41144
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** khangkito - Tran Van Khang (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1334/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. Crafted data in a U3D file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2022-08-19 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory

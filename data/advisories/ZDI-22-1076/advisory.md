# ZDI-22-1076: PDF-XChange Editor submitForm Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1076
- **ZDI-CAN:** ZDI-CAN-17142
- **Date:** 2022-08-18
- **CVE:** CVE-2022-37349
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Suyue Guo and Wei You from Renmin University of China
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the submitForm method. By performing actions in JavaScript, an attacker can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2022-05-16 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory

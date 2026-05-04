# ZDI-22-994: Adobe Acrobat Reader DC PDF Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-994
- **ZDI-CAN:** ZDI-CAN-17018
- **Date:** 2022-07-13
- **CVE:** CVE-2022-34226
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Dennis Herrmann and Sebastian Feldmann
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-994/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. Crafted data in a PDF file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb22-32.html

## Disclosure Timeline

- 2022-06-03 - Vulnerability reported to vendor
- 2022-07-13 - Coordinated public release of advisory

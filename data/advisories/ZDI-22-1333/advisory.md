# ZDI-22-1333: PDF-XChange Editor XPS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1333
- **ZDI-CAN:** ZDI-CAN-18279
- **Date:** 2022-10-07
- **CVE:** CVE-2022-42397
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** khangkito - Tran Van Khang (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1333/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XPS files. Crafted data in an XPS file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.tracker-software.com/product/pdf-xchange-editor/history

## Disclosure Timeline

- 2022-08-19 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory

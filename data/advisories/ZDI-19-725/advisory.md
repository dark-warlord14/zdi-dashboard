# ZDI-19-725: Adobe Acrobat Pro DC AcroForm Bitmap File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-725
- **ZDI-CAN:** ZDI-CAN-8342
- **Date:** 2019-08-19
- **CVE:** CVE-2019-8014
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** ktkitty (https://ktkitty.github.io)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-725/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of run length encoding in BMP images. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-41.html

## Disclosure Timeline

- 2019-05-08 - Vulnerability reported to vendor
- 2019-08-19 - Coordinated public release of advisory
